package com.app;

import javax.imageio.ImageIO;

import com.google.common.collect.Maps;
import org.apache.commons.io.FileUtils;
import org.apache.commons.lang3.StringUtils;

import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.stream.Collectors;

public class ImageClusterBuilder
{
    public static void main(String[] args)
    {
        final ImageClusterBuilder builder = new ImageClusterBuilder();

        try
        {
            builder.buildClusteredImages(60,
                    "/Users/dflores/dariofl24/machinelearn/machineLearningPy/java/ImageKnn/results/points.csv",
                    "/Users/dflores/dariofl24/machinelearn/machineLearningPy/java/ImageKnn/results/klusters.txt",
                    "/Users/dflores/dariofl24/machinelearn/machineLearningPy/java/ImageKnn/inputs/aston.jpg",
                    "/Users/dflores/dariofl24/machinelearn/machineLearningPy/java/ImageKnn/results/clustered");
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
    }

    public void buildClusteredImages(final int maxKlusters, final String pointsFile, final String clustersFile,
            final String imgBase, final String outDir)
            throws IOException
    {
        for (int k = 0; k < maxKlusters; k++)
        {
            System.out.println("BUILDING FOR KLUSTER::" + k);
            final Map<Integer, Map<Integer, ImagePoint>> imageClusterMap = buildImageClusterMap(pointsFile,
                    clustersFile, k);

            buildImage(imgBase, imageClusterMap, new File(outDir, "astonK_" + k + ".jpg"));
        }
    }

    private void buildImage(final String imgBase, final Map<Integer, Map<Integer, ImagePoint>> pointsXIndex,
            final File output)
            throws IOException
    {
        final BufferedImage base = ImageIO.read(new File(imgBase));

        for (int xx = 0; xx < base.getWidth(); xx++)
        {
            final Map<Integer, ImagePoint> pointsYIndex = Optional.ofNullable(pointsXIndex.get(xx))
                    .orElseGet(() -> Maps.newHashMap());

            for (int yy = 0; yy < base.getHeight(); yy++)
            {
                final Color pix = Optional.ofNullable(pointsYIndex.get(yy))
                        .map(point -> point.getColor())
                        .orElseGet(() -> new Color(0.5f, 0.5f, 0.5f, 0f));

                base.setRGB(xx, yy, pix.getRGB());
            }
        }

        ImageIO.write(base, "jpg", output);
    }

    private Map<Integer, Map<Integer, ImagePoint>> buildImageClusterMap(final String pointsFile,
            final String clustersFile, final int kn)
            throws IOException
    {
        final List<String> points = FileUtils.readLines(new File(pointsFile));
        points.remove(0);
        final List<String> clusters = FileUtils.readLines(new File(clustersFile));

        final List<Integer> indexes = clusters.stream()
                .filter(c -> containsCluster(c, kn))
                .map(c -> c.split(",")[0])
                .map(idx -> Integer.parseInt(idx))
                .collect(Collectors.toList());

        System.out.println("Found:" + indexes.size() + " :: " + kn);

        final Map<Integer, Map<Integer, ImagePoint>> pointsXIndex = Maps.newHashMap();

        indexes.stream()
                .map(idx -> points.get(idx))
                .map(point -> point.split(","))
                .map(split -> new ImagePoint(split))
                .forEach(point -> addPointToMap(point, pointsXIndex));

        return pointsXIndex;
    }

    private void addPointToMap(final ImagePoint point, final Map<Integer, Map<Integer, ImagePoint>> pointsXIndex)
    {
        final Map<Integer, ImagePoint> pointsYIndex = Optional.ofNullable(pointsXIndex.get(point.getX()))
                .orElseGet(() -> Maps.newHashMap());

        pointsYIndex.put(point.getY(), point);
        pointsXIndex.put(point.getX(), pointsYIndex);
    }

    private boolean containsCluster(final String string, final int kn)
    {
        return (StringUtils.isEmpty(string)) ? false : string.endsWith("," + kn);
    }
}
