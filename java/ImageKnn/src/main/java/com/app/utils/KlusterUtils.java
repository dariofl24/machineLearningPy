package com.app.utils;

import com.google.common.collect.ImmutableList;
import com.google.common.collect.Lists;
import com.google.common.collect.Maps;
import org.apache.commons.io.FileUtils;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.Random;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;
import java.util.stream.Collectors;

public class KlusterUtils
{
    public static void main(String[] args)
    {
        final File file = new File(
                "/Users/dflores/dariofl24/machinelearn/machineLearningPy/java/ImageKnn/results/colors.csv");

        final KlusterUtils utils = new KlusterUtils();

        final KlusterResult klusters = utils.getKlustersFromCSV(file, 60, 4);

        klusters.getLabelKlusterMap().entrySet().stream().forEach(System.out::println);
        klusters.getKlusterPointsMap().entrySet().stream()
                .forEach(entry -> System.out.println(entry.getKey() + "\t" + entry.getValue().size()));
    }

    public KlusterResult getKlustersFromCSV(final File file, final Integer kn, final int randState)
    {
        try
        {
            final List<String> strings = FileUtils.readLines(file);

            strings.remove(0);

            final List<ImmutableList<Double>> collect = strings.stream().map(ss -> ss.split(","))
                    .map(this::toDoubleArr)
                    .map(list -> ImmutableList.<Double>builder().addAll(list).build())
                    .collect(Collectors.toList());

            return getKlusters(collect, kn, randState);
        }
        catch (IOException e)
        {
            e.printStackTrace();
            return null;
        }
    }

    public List<Double> toDoubleArr(final String[] arr)
    {
        return Arrays.stream(arr).map(Double::valueOf).collect(Collectors.toList());
    }

    public KlusterResult getKlusters(final List<ImmutableList<Double>> points, final Integer kn, final int randState)
    {
        Map<Integer, ImmutableList<Double>> initialKlusters = generateInitialKlusters2(points, kn, randState);

        boolean next = true;

        HashMap<Integer, List<ImmutableList<Double>>> klusterPointsMap = null;
        Map<Integer, ImmutableList<Double>> newKlusters = null;

        while (next)
        {
            try
            {
                klusterPointsMap = assignPointsToKlustersParallel(initialKlusters, points);
            }
            catch (InterruptedException e)
            {
                e.printStackTrace();
            }

            newKlusters = klusterPointsMap.entrySet().stream()
                    .map(this::calculateCentroidFromEntry)
                    .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));

            next = !areEqual(initialKlusters, newKlusters, 0.000001);
            initialKlusters = newKlusters;
        }

        return new KlusterResult(klusterPointsMap, newKlusters);
    }

    private boolean areEqual(final Map<Integer, ImmutableList<Double>> initialKlusters,
            final Map<Integer, ImmutableList<Double>> newKlusters, final Double precision)
    {
        //System.out.println("-----------");
        for (final Integer key : initialKlusters.keySet())
        {

            if (newKlusters.containsKey(key))
            {
                final ImmutableList<Double> vec1 = initialKlusters.get(key);
                final ImmutableList<Double> vec2 = newKlusters.get(key);

                final Double distance = distance(vec1, vec2);
                //System.out.println(distance);

                if (distance.compareTo(precision) > 0)
                {
                    return false;
                }
            }
        }

        return true;
    }

    private Map.Entry<Integer, ImmutableList<Double>> calculateCentroidFromEntry(
            final Map.Entry<Integer, List<ImmutableList<Double>>> entry)
    {
        final List<ImmutableList<Double>> points = entry.getValue();

        return Map.entry(entry.getKey(), calculateCentroid(points));
    }

    private ImmutableList<Double> calculateCentroid(final List<ImmutableList<Double>> points)
    {
        final int dimension = points.stream().findFirst().get().size();

        final ImmutableList.Builder<Double> builder = ImmutableList.<Double>builder();

        for (int axis = 0; axis < dimension; axis++)
        {
            final int ii = axis;
            final Double collect = points.stream().map(point -> point.get(ii))
                    .collect(Collectors.summingDouble(Double::doubleValue));

            builder.add(collect / (double) points.size());
        }

        return builder.build();
    }

    private HashMap<Integer, List<ImmutableList<Double>>> assignPointsToKlusters(
            final Map<Integer, ImmutableList<Double>> klusters,
            final List<ImmutableList<Double>> points)
    {
        final HashMap<Integer, List<ImmutableList<Double>>> klusterPointMap = Maps.newHashMap();

        for (final ImmutableList<Double> point : points)
        {
            final Integer kluster = pointBelongsToKluster(point, klusters);

            if (!klusterPointMap.containsKey(kluster))
            {
                klusterPointMap.put(kluster, Lists.newArrayList());
            }

            klusterPointMap.get(kluster).add(point);
        }

        return klusterPointMap;
    }

    private HashMap<Integer, List<ImmutableList<Double>>> assignPointsToKlustersParallel(
            final Map<Integer, ImmutableList<Double>> klusters,
            final List<ImmutableList<Double>> points) throws InterruptedException
    {
        final int partitions = (int) Math.ceil(points.size() / 100);

        final List<Future<HashMap<Integer, List<ImmutableList<Double>>>>> partial = Lists.newArrayList();
        final List<HashMap<Integer, List<ImmutableList<Double>>>> results = Lists.newArrayList();

        for (int i = 0; i < partitions; i++)
        {
            final int upperlim = (i + 1) * 100;
            final List<ImmutableList<Double>> subList = points
                    .subList(i * 100, (upperlim >= points.size()) ? points.size() : upperlim);

            final Future<HashMap<Integer, List<ImmutableList<Double>>>> hashMapFuture = calculateAsync(subList,
                    klusters);

            if (partial.size() < 10)
            {
                partial.add(hashMapFuture);
            }
            else
            {
                partial.stream().map(future -> {
                    try
                    {
                        return future.get();
                    }
                    catch (InterruptedException | ExecutionException e)
                    {
                        e.printStackTrace();
                        return null;
                    }
                }).forEach(results::add);

                partial.clear();
            }
        }

        final HashMap<Integer, List<ImmutableList<Double>>> resultMap = Maps.newHashMap();

        for (final HashMap<Integer, List<ImmutableList<Double>>> partialMap : results)
        {
            for (final Integer key : partialMap.keySet())
            {
                if (!resultMap.containsKey(key))
                {
                    resultMap.put(key, Lists.newArrayList());
                }

                resultMap.get(key).addAll(partialMap.get(key));
            }
        }

        return resultMap;
    }

    public Future<HashMap<Integer, List<ImmutableList<Double>>>> calculateAsync(
            final List<ImmutableList<Double>> subList,
            final Map<Integer, ImmutableList<Double>> klusters) throws InterruptedException
    {
        return CompletableFuture.supplyAsync(() -> CalculationWorker.getInstance()
                .assignPointsToKlusters(subList, klusters));
    }

    private Integer pointBelongsToKluster(final ImmutableList<Double> point,
            final Map<Integer, ImmutableList<Double>> klusters)
    {
        final Map<Double, Integer> distanceKluster = Maps.newHashMap();

        klusters.entrySet()
                .forEach(entry -> distanceKluster.put(this.distanceSqrt(point, entry.getValue()), entry.getKey()));

        final Optional<Double> min = distanceKluster.keySet().stream().min(Comparator.naturalOrder());

        return distanceKluster.get(min.get());
    }

    public Map<Integer, ImmutableList<Double>> generateInitialKlusters2(final List<ImmutableList<Double>> points,
            final Integer kn, final int randState)
    {
        List<ImmutableList<Double>> dest1 = Lists.newArrayList(points);

        Collections.copy(dest1, points);

        Map<Integer, ImmutableList<Double>> klusters = Maps.newHashMap();

        for (int i = 0; i < kn; i++)
        {
            Collections.shuffle(dest1, new Random(i + 2 + randState));
            klusters.put(i, dest1.get(i));
        }

        return klusters;
    }

    private Double distanceSqrt(final ImmutableList<Double> a, final ImmutableList<Double> b)
    {
        final ArrayList<Double> dif = Lists.newArrayList();

        for (int idx = 0; idx < a.size(); idx++)
        {
            dif.add(Math.pow(a.get(idx) - b.get(idx), 2d));
        }

        return dif.stream().collect(Collectors.summingDouble(Double::doubleValue));
    }

    private Double distance(final ImmutableList<Double> a, final ImmutableList<Double> b)
    {
        return Math.sqrt(distanceSqrt(a, b));
    }

    public static class KlusterResult
    {
        private HashMap<Integer, List<ImmutableList<Double>>> klusterPointsMap;

        private Map<Integer, ImmutableList<Double>> labelKlusterMap;

        public KlusterResult(
                final HashMap<Integer, List<ImmutableList<Double>>> klusterPointsMap,
                final Map<Integer, ImmutableList<Double>> labelKlusterMap)
        {
            this.klusterPointsMap = klusterPointsMap;
            this.labelKlusterMap = labelKlusterMap;
        }

        public HashMap<Integer, List<ImmutableList<Double>>> getKlusterPointsMap()
        {
            return klusterPointsMap;
        }

        public Map<Integer, ImmutableList<Double>> getLabelKlusterMap()
        {
            return labelKlusterMap;
        }
    }

    private static class CalculationWorker
    {
        public static CalculationWorker getInstance()
        {
            return new CalculationWorker();
        }

        private HashMap<Integer, List<ImmutableList<Double>>> assignPointsToKlusters(
                final List<ImmutableList<Double>> points,
                final Map<Integer, ImmutableList<Double>> klusters)
        {
            final HashMap<Integer, List<ImmutableList<Double>>> klusterPointMap = Maps.newHashMap();

            for (final ImmutableList<Double> point : points)
            {
                final Integer kluster = pointBelongsToKluster(point, klusters);

                if (!klusterPointMap.containsKey(kluster))
                {
                    klusterPointMap.put(kluster, Lists.newArrayList());
                }

                klusterPointMap.get(kluster).add(point);
            }

            return klusterPointMap;
        }

        private Integer pointBelongsToKluster(final ImmutableList<Double> point,
                final Map<Integer, ImmutableList<Double>> klusters)
        {
            final Map<Double, Integer> distanceKluster = Maps.newHashMap();

            klusters.entrySet()
                    .forEach(entry -> distanceKluster.put(distanceSqrt(point, entry.getValue()), entry.getKey()));

            final Optional<Double> min = distanceKluster.keySet().stream().min(Comparator.naturalOrder());

            return distanceKluster.get(min.get());
        }

        private Double distanceSqrt(final ImmutableList<Double> a, final ImmutableList<Double> b)
        {
            final ArrayList<Double> dif = Lists.newArrayList();

            for (int idx = 0; idx < a.size(); idx++)
            {
                dif.add(Math.pow(a.get(idx) - b.get(idx), 2d));
            }

            return dif.stream().collect(Collectors.summingDouble(Double::doubleValue));
        }
    }
}
