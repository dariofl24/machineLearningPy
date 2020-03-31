package com.app.builder;

import javax.imageio.ImageIO;

import com.app.utils.KlusterUtils;
import com.google.common.collect.ImmutableList;
import com.google.common.collect.Lists;
import com.google.common.collect.Maps;
import org.apache.commons.io.FileUtils;
import org.apache.commons.lang3.StringUtils;

import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;

public class ImageColorClusterBuilder
{
    private Integer max_clusters = 0;

    public static void main(String[] args)
    {
        final ImageColorClusterBuilder builder = new ImageColorClusterBuilder();

        try
        {
            builder.build("/Users/dflores/dariofl24/machinelearn/machineLearningPy/java/ImageKnn/results/colors.csv",
                    "/Users/dflores/dariofl24/machinelearn/machineLearningPy/java/ImageKnn/results/colors_klusters.txt",
                    "/Users/dflores/dariofl24/machinelearn/machineLearningPy/java/ImageKnn/inputs/aston22.jpg",
                    "/Users/dflores/dariofl24/machinelearn/machineLearningPy/java/ImageKnn/results/colors",
                    false);
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
    }

    public void build(final String colors, final String colors_klusters, final String imgBase,
            final String outputPath, final boolean greyScale)
            throws IOException
    {
        //final HashMap<String, Integer> colorKlusterMap = parseColorClusterInfo(colors, colors_klusters);
        max_clusters = 8;
        final HashMap<String, Integer> colorKlusterMap = calculateKlusters(colors, max_clusters);

        for (int knx = 0; knx < max_clusters; knx++)
        {
            System.out.println("Building:" + knx);
            buildImage(imgBase, colorKlusterMap,
                    new File(outputPath, "ck_" + knx + ".jpg"),
                    Lists.newArrayList(knx), greyScale);
        }
    }

    private void buildImage(final String imgBase, final HashMap<String, Integer> colorKlusterMap,
            final File output, final List<Integer> knns, final boolean greyScale)
            throws IOException
    {
        final BufferedImage base = ImageIO.read(new File(imgBase));

        final Color pix = new Color(0.5f, 0.5f, 0.5f, 0f);

        for (int xx = 0; xx < base.getWidth(); xx++)
        {
            for (int yy = 0; yy < base.getHeight(); yy++)
            {
                final Color color = new Color(base.getRGB(xx, yy));
                final String key = color.getRed() + "," + color.getGreen() + "," + color.getBlue();

                if (!knns.contains(colorKlusterMap.get(key)))
                {
                    base.setRGB(xx, yy, pix.getRGB());
                }
                else
                {
                    base.setRGB(xx, yy, getGrayScaleColor(color, greyScale).getRGB());
                }
            }
        }

        ImageIO.write(base, "jpg", output);
    }

    private static final double SQRT_3 = Math.sqrt(3d);

    private Color getGrayScaleColor(final Color color, final boolean greyScale)
    {
        if (!greyScale)
            return color;

        final int red = color.getRed();
        final int green = color.getGreen();
        final int blue = color.getBlue();

        final int rgb = (int) Math.round(
                (Math.sqrt((red * red) + (green * green) + (blue * blue)) / SQRT_3) * 0.70
        );

        return new Color(rgb, rgb, rgb);
    }

    private HashMap<String, Integer> calculateKlusters(final String colors, final Integer kn)
    {
        final File file = new File(colors);

        final KlusterUtils utils = new KlusterUtils();

        final KlusterUtils.KlusterResult klusters = utils.getKlustersFromCSV(file, kn, 4);

        final HashMap<Integer, List<ImmutableList<Double>>> klusterPointsMap = klusters.getKlusterPointsMap();

        final HashMap<String, Integer> resp = Maps.newHashMap();

        for (final Integer key : klusterPointsMap.keySet())
        {
            final List<ImmutableList<Double>> immutableLists = klusterPointsMap.get(key);

            for (final ImmutableList<Double> point : immutableLists)
            {
                final String stringVector = toStringVector(point);
                resp.put(stringVector, key);
            }
        }

        return resp;
    }

    private String toStringVector(final ImmutableList<Double> point)
    {
        return point.stream().map(dd -> dd.toString()).map(ss -> ss.replaceAll("\\.\\d*", ""))
                .collect(Collectors.joining(","));
    }

    private HashMap<String, Integer> parseColorClusterInfo(final String colors, final String clusters)
            throws IOException
    {
        final List<String> colorsList = FileUtils.readLines(new File(colors))
                .stream()
                .filter(StringUtils::isNotEmpty)
                .collect(Collectors.toList());
        colorsList.remove(0);

        final List<Integer> clustersList = FileUtils.readLines(new File(clusters))
                .stream()
                .filter(StringUtils::isNotEmpty)
                .map(str -> str.split(",")[1])
                .map(Integer::parseInt)
                .collect(Collectors.toList());

        max_clusters = clustersList.stream().max(Comparator.naturalOrder()).get();

        System.out.println("MAX_CLUSTERS: " + max_clusters);
        System.out.println("FOUND: " + colorsList.size() + "," + clustersList.size());

        final HashMap<String, Integer> colorKlusterMap = Maps.newHashMap();

        for (int ii = 0; ii < colorsList.size(); ii++)
        {
            final String cc = colorsList.get(ii);
            final Integer kk = clustersList.get(ii);

            colorKlusterMap.put(cc, kk);
        }

        return colorKlusterMap;
    }
}
