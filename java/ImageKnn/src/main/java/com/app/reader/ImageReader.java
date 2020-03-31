package com.app.reader;

import javax.imageio.ImageIO;

import com.app.ImagePoint;
import com.google.common.collect.Lists;
import com.google.common.collect.Sets;
import org.apache.commons.io.FileUtils;

import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

public class ImageReader
{
    public static void main(String[] args)
    {
        try
        {
            ImageReader
                    .imageRead("/Users/dflores/dariofl24/machinelearn/machineLearningPy/java/ImageKnn/inputs/aston22.jpg",
                            "/Users/dflores/dariofl24/machinelearn/machineLearningPy/java/ImageKnn/results/points.csv",
                            "/Users/dflores/dariofl24/machinelearn/machineLearningPy/java/ImageKnn/results/colors.csv");
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
    }

    public static void imageRead(final String imgFile, final String outPoints, final String outColors)
            throws IOException
    {
        final BufferedImage image = ImageIO.read(new File(imgFile));

        final ArrayList<ImagePoint> points = Lists.newArrayList();
        final Set<Color> colors = Sets.newHashSet();

        System.out.println(image.getWidth() + "," + image.getHeight());

        for (int xx = 0; xx < image.getWidth(); xx++)
        {
            for (int yy = 0; yy < image.getHeight(); yy++)
            {
                final Color color = new Color(image.getRGB(xx, yy));

                points.add(new ImagePoint(xx, yy, color.getRed(), color.getGreen(), color.getBlue()));
                colors.add(color);
            }
        }

        final List<String> colorArrayList = Lists.newArrayList(colors.iterator()).stream()
                .map(color -> (color.getRed() + "," + color.getGreen() + "," + color.getBlue()))
                .collect(Collectors.toList());

        colorArrayList.add(0, "r,g,b");

        FileUtils.writeLines(new File(outColors), colorArrayList);

        final List<String> pointsList =
                points.stream().map(ImagePoint::toString).collect(Collectors.toList());

        pointsList.add(0, "x,y,r,g,b,n");

        FileUtils.writeLines(new File(outPoints), pointsList);
    }
}
