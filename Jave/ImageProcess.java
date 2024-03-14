import java.awt.Color;
import java.awt.image.BufferedImage;
import java.io.File;
import java.net.URL;
import java.util.Arrays;
import java.util.Random;
import javax.imageio.ImageIO;
public class ImageProcessing {
	public static void main(String[] args) {
        // The provided images are apple.jpg, flower.jpg, and kitten.jpg
		int[][] imageData = imgToTwoD("./kitten.jpg");
         // Or load your own image using a URL!
		//int[][] imageData = imgToTwoD("https://content.codecademy.com/projects/project_thumbnails/phaser/bug-dodger.png");
		//viewImageData(imageData);
		int[][] trimmed = trimBorders(imageData, 60);
		twoDToImage(trimmed, "./trimmed_kitten.jpg");

        int[][] negative = negativeColor(imageData);
        twoDToImage(negative, "./negative_kitten.jpg");

        int[][] stretch = stretchHorizontally(imageData);
        twoDToImage(stretch, "./stretched_kitten.jpg");

        int[][] verticalShrink = shrinkVertically(imageData);
        twoDToImage(verticalShrink, "./vertical_shrink_kitten.jpg");

        int[][] invert = invertImage(imageData);
        twoDToImage(invert, "./inverted_kitten.jpg");

        int[][] filter = colorFilter(imageData, -75, 30, -30);
        twoDToImage(filter, "./filtered_kitten.jpg");

        int[][] canvas = new int[500][500];
        paintRandomImage(canvas);
        twoDToImage(canvas, "./painted_canvas.jpg");

        int[] rgba = {0, 255, 255, 255};
        int colour = getColorIntValFromRGBA(rgba);
        int[][] drawRectangle = paintRectangle(imageData, 50, 80, 100, 80, colour);
        twoDToImage(drawRectangle, "./draw_rectangle.jpg");

        int[][] generateRectangles = generateRectangles(imageData, 1000);
        twoDToImage(generateRectangles, "./generate_rectangles.jpg");

		int[][] allFilters = stretchHorizontally(shrinkVertically(colorFilter(negativeColor(trimBorders(invertImage(imageData), 50)), 200, 20, 40)));
        twoDToImage(allFilters, "./all_filtered.jpg");
		// Painting with pixels
	}
	// Image Processing Methods
	public static int[][] trimBorders(int[][] imageTwoD, int pixelCount) {
		// Example Method
		if (imageTwoD.length > pixelCount * 2 && imageTwoD[0].length > pixelCount * 2) {
			int[][] trimmedImg = new int[imageTwoD.length - pixelCount * 2][imageTwoD[0].length - pixelCount * 2];
			for (int i = 0; i < trimmedImg.length; i++) {
				for (int j = 0; j < trimmedImg[i].length; j++) {
					trimmedImg[i][j] = imageTwoD[i + pixelCount][j + pixelCount];
				}
			}
			return trimmedImg;
		} else {
			System.out.println("Cannot trim that many pixels from the given image.");
			return imageTwoD;
		}
	}
	public static int[][] negativeColor(int[][] imageTwoD) {
		// TODO: Fill in the code for this method
    int[][] colourInvertedImg = new int[imageTwoD.length][imageTwoD[0].length];
    for (int i = 0; i < imageTwoD.length; i++) {
      for (int j = 0; j < imageTwoD[0].length; j++) {
        int[] rgba = getRGBAFromPixel(imageTwoD[i][j]);
        rgba[0] = 255 - rgba[0];
        rgba[1] = 255 - rgba[1];
        rgba[2] = 255 - rgba[2];
        colourInvertedImg[i][j] = getColorIntValFromRGBA(rgba);
      }
    }
		return colourInvertedImg;
	}
	public static int[][] stretchHorizontally(int[][] imageTwoD) {
		// TODO: Fill in the code for this method
    int[][] stretchedImage = new int[imageTwoD.length][imageTwoD[0].length*2];
    for (int i = 0; i < imageTwoD.length; i++) {
      for (int j = 0; j < imageTwoD[0].length; j++) {
        int currentPosition = j * 2;
        stretchedImage[i][currentPosition] = imageTwoD[i][j];
        stretchedImage[i][currentPosition+1] = imageTwoD[i][j];
      }
    }
		return stretchedImage;
	}
	public static int[][] shrinkVertically(int[][] imageTwoD) {
		// TODO: Fill in the code for this method
    int[][] verticallyShrinkedImage = new int[imageTwoD.length / 2][imageTwoD[0].length];
    for (int i = 0; i < imageTwoD[0].length; i++) {
      for (int j = 0; j < imageTwoD.length-1; j+=2) {
        verticallyShrinkedImage[j/2][i] = imageTwoD[j][i];
      }
    }
		return verticallyShrinkedImage;
	}
	public static int[][] invertImage(int[][] imageTwoD) {
    // TODO: Fill in the code for this method
    int[][] invertedImage = new int[imageTwoD.length][imageTwoD[0].length];
    for (int i = 0; i < imageTwoD.length; i++) {
      for (int j = 0; j < imageTwoD[0].length; j++) {
        invertedImage[i][j] = imageTwoD[(imageTwoD.length-1)-i][(imageTwoD[i].length-1)-j];
      }
    }
		return invertedImage;
	}
	public static int[][] colorFilter(int[][] imageTwoD, int redChangeValue, int greenChangeValue, int blueChangeValue) {
		// TODO: Fill in the code for this method
    int[][] modifiedImg = new int[imageTwoD.length][imageTwoD[0].length];
    for (int i = 0; i < imageTwoD.length; i++) {
      for (int j = 0; j < imageTwoD[0].length; j++) {
        int[] rgba = getRGBAFromPixel(imageTwoD[i][j]);
        int newRed = rgba[0] + redChangeValue;
        int newGreen = rgba[1] + greenChangeValue;
        int newBlue = rgba[2] + blueChangeValue;
        if (newRed < 0) {
          newRed = 0;
        } else if (newRed > 255) {
          newRed = 255;
        }
        if (newGreen < 0) {
          newGreen = 0;
        } else if (newGreen > 255) {
          newGreen = 255;
        }
        if (newBlue < 0) {
          newBlue = 0;
        } else if (newBlue > 255) {
          newBlue = 255;
        }
        rgba[0] = newRed;
        rgba[1] = newGreen;
        rgba[2] = newBlue;
        modifiedImg[i][j] = getColorIntValFromRGBA(rgba);
      }
    }
		return modifiedImg;
	}
	// Painting Methods
	public static int[][] paintRandomImage(int[][] canvas) {
		// TODO: Fill in the code for this method
    Random rand = new Random();
    for (int i = 0; i < canvas.length; i++) {
      for (int j = 0; j < canvas[0].length; j++) {
        int randRed = rand.nextInt(256);
        int randGreen = rand.nextInt(256);
        int randBlue = rand.nextInt(256);
        int[] rgbaValues = {randRed, randGreen, randBlue, 255};
        canvas[i][j] = getColorIntValFromRGBA(rgbaValues);
      }
    }
		return canvas;
	}
	public static int[][] paintRectangle(int[][] canvas, int width, int height, int rowPosition, int colPosition, int color) {
		// TODO: Fill in the code for this method
    for (int i = 0; i < canvas.length; i++) {
      for (int j = 0; j < canvas[0].length; j++) {
        if (i >= rowPosition && i <= rowPosition + width) {
          if (j >= colPosition && j <= colPosition + height) {
            canvas[i][j] = color;
          }
        }
      }
    }
		return canvas;
	}
	public static int[][] generateRectangles(int[][] canvas, int numRectangles) {
		// TODO: Fill in the code for this method
    Random rand = new Random();
    for (int i = 0; i < numRectangles; i++) {
      int randomWidth = rand.nextInt(canvas[0].length);
      int randomHeight = rand.nextInt(canvas.length);
      int randomRowPosition = rand.nextInt(canvas.length - randomHeight);
      int randomColPosition = rand.nextInt(canvas[0].length - randomWidth);
      int randRed = rand.nextInt(256);
      int randGreen = rand.nextInt(256);
      int randBlue = rand.nextInt(256);
      int[] rgbaValues = {randRed, randGreen, randBlue, 255};
      int randomColour = getColorIntValFromRGBA(rgbaValues);
      canvas = paintRectangle(canvas, randomWidth, randomHeight, randomRowPosition, randomColPosition, randomColour);
    }
		return canvas;
	}
	// Utility Methods
	public static int[][] imgToTwoD(String inputFileOrLink) {
		try {
			BufferedImage image = null;
			if (inputFileOrLink.substring(0, 4).toLowerCase().equals("http")) {
				URL imageUrl = new URL(inputFileOrLink);
				image = ImageIO.read(imageUrl);
				if (image == null) {
					System.out.println("Failed to get image from provided URL.");
				}
			} else {
				image = ImageIO.read(new File(inputFileOrLink));
			}
			int imgRows = image.getHeight();
			int imgCols = image.getWidth();
			int[][] pixelData = new int[imgRows][imgCols];
			for (int i = 0; i < imgRows; i++) {
				for (int j = 0; j < imgCols; j++) {
					pixelData[i][j] = image.getRGB(j, i);
				}
			}
			return pixelData;
		} catch (Exception e) {
			System.out.println("Failed to load image: " + e.getLocalizedMessage());
			return null;
		}
	}
	public static void twoDToImage(int[][] imgData, String fileName) {
		try {
			int imgRows = imgData.length;
			int imgCols = imgData[0].length;
			BufferedImage result = new BufferedImage(imgCols, imgRows, BufferedImage.TYPE_INT_RGB);
			for (int i = 0; i < imgRows; i++) {
				for (int j = 0; j < imgCols; j++) {
					result.setRGB(j, i, imgData[i][j]);
				}
			}
			File output = new File(fileName);
			ImageIO.write(result, "jpg", output);
		} catch (Exception e) {
			System.out.println("Failed to save image: " + e.getLocalizedMessage());
		}
	}
	public static int[] getRGBAFromPixel(int pixelColorValue) {
		Color pixelColor = new Color(pixelColorValue);
		return new int[] { pixelColor.getRed(), pixelColor.getGreen(), pixelColor.getBlue(), pixelColor.getAlpha() };
	}
	public static int getColorIntValFromRGBA(int[] colorData) {
		if (colorData.length == 4) {
			Color color = new Color(colorData[0], colorData[1], colorData[2], colorData[3]);
			return color.getRGB();
		} else {
			System.out.println("Incorrect number of elements in RGBA array.");
			return -1;
		}
	}
	public static void viewImageData(int[][] imageTwoD) {
		if (imageTwoD.length > 3 && imageTwoD[0].length > 3) {
			int[][] rawPixels = new int[3][3];
			for (int i = 0; i < 3; i++) {
				for (int j = 0; j < 3; j++) {
					rawPixels[i][j] = imageTwoD[i][j];
				}
			}
			System.out.println("Raw pixel data from the top left corner.");
			System.out.print(Arrays.deepToString(rawPixels).replace("],", "],\n") + "\n");
			int[][][] rgbPixels = new int[3][3][4];
			for (int i = 0; i < 3; i++) {
				for (int j = 0; j < 3; j++) {
					rgbPixels[i][j] = getRGBAFromPixel(imageTwoD[i][j]);
				}
			}
			System.out.println();
			System.out.println("Extracted RGBA pixel data from top the left corner.");
			for (int[][] row : rgbPixels) {
				System.out.print(Arrays.deepToString(row) + System.lineSeparator());
			}
		} else {
			System.out.println("The image is not large enough to extract 9 pixels from the top left corner");
		}
	}
}