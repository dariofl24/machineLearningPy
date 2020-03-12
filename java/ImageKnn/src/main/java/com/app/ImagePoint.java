package com.app;

import java.awt.*;

public class ImagePoint
{
    private Integer x;

    private Integer y;

    private Integer r;

    private Integer g;

    private Integer b;

    public ImagePoint(final String[] arr)
    {
        this.x = Integer.parseInt(arr[0]);
        this.y = Integer.parseInt(arr[1]);
        this.r = Integer.parseInt(arr[2]);
        this.g = Integer.parseInt(arr[3]);
        this.b = Integer.parseInt(arr[4]);
    }

    public ImagePoint(final Integer x, final Integer y, final Integer r, final Integer g, final Integer b)
    {
        this.x = x;
        this.y = y;
        this.r = r;
        this.g = g;
        this.b = b;
    }

    public Integer getX()
    {
        return x;
    }

    public void setX(final Integer x)
    {
        this.x = x;
    }

    public Integer getY()
    {
        return y;
    }

    public void setY(final Integer y)
    {
        this.y = y;
    }

    public Integer getR()
    {
        return r;
    }

    public void setR(final Integer r)
    {
        this.r = r;
    }

    public Integer getG()
    {
        return g;
    }

    public void setG(final Integer g)
    {
        this.g = g;
    }

    public Integer getB()
    {
        return b;
    }

    public void setB(final Integer b)
    {
        this.b = b;
    }

    public Color getColor()
    {
        return new Color(r, g, b);
    }

    @Override
    public String toString()
    {
        final int normSqrt = (r * r) + (g * g) + (b * b);

        return x + "," + y + "," + r + "," + g + "," + b + "," + 0;
    }
}
