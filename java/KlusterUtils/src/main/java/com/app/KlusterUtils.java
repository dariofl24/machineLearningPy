package com.app;

import com.google.common.collect.ImmutableList;
import com.google.common.collect.Lists;
import com.google.common.collect.Maps;

import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class KlusterUtils
{
    public static void main(String[] args)
    {
        final List<ImmutableList<Double>> points = Lists.newArrayList();

        points.add(ImmutableList.of(0d, 101d));
        points.add(ImmutableList.of(1d, 102d));
        points.add(ImmutableList.of(2d, 103d));
        points.add(ImmutableList.of(3d, 104d));
        points.add(ImmutableList.of(4d, 105d));
        points.add(ImmutableList.of(5d, 106d));
        points.add(ImmutableList.of(6d, 107d));
        points.add(ImmutableList.of(7d, 108d));
        points.add(ImmutableList.of(8d, 109d));
        points.add(ImmutableList.of(9d, 110d));

        KlusterUtils utils = new KlusterUtils();

        final List<ImmutableList<Double>> initialKlusters = utils.generateInitialKlusters(points, 15);

        initialKlusters.stream().forEach(point -> {
            System.out.println(point.stream().map(xx -> xx.toString()).collect(Collectors.joining(",")));
        });
    }

    public List<ImmutableList<Double>> generateInitialKlusters(final List<ImmutableList<Double>> points,
            final Integer kn)
    {
        final HashMap<Integer, List<Double>> axisMap = Maps.newHashMap();

        for (final ImmutableList<Double> point : points)
        {
            for (Integer idx = 0; idx < point.size(); idx++)
            {
                addToMap(idx, point.get(idx), axisMap);
            }
        }

        final Double[][] kMatrix = new Double[axisMap.keySet().size()][kn];

        for (final Integer axis : axisMap.keySet())
        {
            final Double min = axisMap.get(axis).stream().min(Comparator.naturalOrder()).get();
            final Double max = axisMap.get(axis).stream().max(Comparator.naturalOrder()).get();

            addCoordinatesToMatrix(min, max, kn, kMatrix, axis);
        }

        final List<ImmutableList<Double>> initialKlusters = Lists.newArrayList();

        for (int k = 0; k < kn; k++)
        {
            final ImmutableList.Builder<Double> builder = ImmutableList.<Double>builder();

            for (int axis = 0; axis < axisMap.keySet().size(); axis++)
            {
                builder.add(kMatrix[axis][k]);
            }

            initialKlusters.add(builder.build());
        }

        return initialKlusters;
    }

    private void addCoordinatesToMatrix(final Double min, final Double max, final Integer kn,
            final Double[][] kMatrix, final Integer axis)
    {
        final double delta = max - min;

        for (int k = 0; k < kn; k++)
        {
            final Double coordinate = (delta * Math.random()) + min;

            kMatrix[axis][k] = coordinate;
        }
    }

    private void addToMap(final Integer idx, final Double value, final Map<Integer, List<Double>> map)
    {
        if (!map.containsKey(idx))
        {
            map.put(idx, Lists.newArrayList());
        }

        map.get(idx).add(value);
    }
}
