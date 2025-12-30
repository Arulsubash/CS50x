#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int avrage;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            avrage =
                round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0);
            image[i][j].rgbtBlue = avrage;
            image[i][j].rgbtGreen = avrage;
            image[i][j].rgbtRed = avrage;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int Red;
    int Green;
    int Blue;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            Red = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen +
                        .189 * image[i][j].rgbtBlue);
            Green = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen +
                          .168 * image[i][j].rgbtBlue);
            Blue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen +
                         .131 * image[i][j].rgbtBlue);
            if (Red > 255)
            {
                Red = 255;
            }
            if (Green > 255)
            {
                Green = 255;
            }
            if (Blue > 255)
            {
                Blue = 255;
            }
            image[i][j].rgbtRed = Red;
            image[i][j].rgbtGreen = Green;
            image[i][j].rgbtBlue = Blue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE buffer;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            buffer = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = buffer;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float red = 0, green = 0, blue = 0, total = 0;
            for (int updated_i = i - 1; updated_i < i + 2; updated_i++)
            {
                for (int updated_j = j - 1; updated_j < j + 2; updated_j++)
                {
                    if (updated_i >= 0 && updated_j >= 0 && updated_i < height && updated_j < width)
                    {
                        red += image[updated_i][updated_j].rgbtRed;
                        green += image[updated_i][updated_j].rgbtGreen;
                        blue += image[updated_i][updated_j].rgbtBlue;
                        total++;
                    }
                }
            }
            copy[i][j].rgbtRed = round(red / total);
            copy[i][j].rgbtGreen = round(green / total);
            copy[i][j].rgbtBlue = round(blue / total);
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = copy[i][j];
        }
    }
    return;
}
