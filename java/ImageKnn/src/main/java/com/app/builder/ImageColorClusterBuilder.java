package com.app.builder;

import javax.imageio.ImageIO;

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
                    "/Users/dflores/dariofl24/machinelearn/machineLearningPy/java/ImageKnn/inputs/aston.jpg",
                    "/Users/dflores/dariofl24/machinelearn/machineLearningPy/java/ImageKnn/results/colors");
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
    }

    public void build(final String colors, final String colors_klusters, final String imgBase,
            final String outputPath)
            throws IOException
    {
        final HashMap<String, Integer> colorKlusterMap = parseColorClusterInfo(colors, colors_klusters);

        for (int kn = 0; kn <= max_clusters; kn++)
        {
            System.out.println("Building:" + kn);
            buildImage(imgBase, colorKlusterMap, new File(outputPath, "ck_" + kn + ".jpg"), kn);
        }
    }

    private void buildImage(final String imgBase, final HashMap<String, Integer> colorKlusterMap,
            final File output, final int knn)
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

                if (colorKlusterMap.get(key) != knn)
                {
                    base.setRGB(xx, yy, pix.getRGB());
                }
            }
        }

        ImageIO.write(base, "jpg", output);
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
