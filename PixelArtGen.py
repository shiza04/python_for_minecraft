from PIL import Image
import sys

blocks = {"black_concrete": (8, 10, 15),
          "black_concrete_powder": (25, 27, 32),
          "black_terracotta": (37, 23, 16, 255),
          "black_wool": (21, 21, 26),
          "blue_concrete": (45, 47, 143),
          "blue_concrete_powder": (70, 73, 167),
          "blue_terracotta": (74, 60, 91, 255),
          "blue_wool": (53, 57, 157),
          "brown_concrete": (96, 60, 32),
          "brown_concrete_powder": (126, 85, 54),
          "brown_terracotta": (77, 51, 36, 255),
          "brown_wool": (114, 72, 41),
          "cyan_concrete": (21, 119, 136),
          "cyan_concrete_powder": (37, 148, 157),
          "cyan_terracotta": (87, 91, 91, 255),
          "cyan_wool": (21, 138, 145),
          "gray_concrete": (55, 58, 62),
          "gray_concrete_powder": (77, 81, 85),
          "gray_terracotta": (58, 42, 36, 255),
          "gray_wool": (63, 68, 72),
          "green_concrete": (73, 91, 36),
          "green_concrete_powder": (97, 119, 45),
          "green_terracotta": (76, 83, 42, 255),
          "green_wool": (85, 110, 27),
          "light_blue_concrete": (36, 137, 199),
          "light_blue_concrete_powder": (74, 181, 214),
          "light_blue_terracotta": (114, 109, 138, 255),
          "light_blue_wool": (58, 175, 217),
          "light_gray_concrete": (125, 125, 115),
          "light_gray_concrete_powder": (155, 155, 148),
          "light_gray_terracotta": (135, 107, 98, 255),
          "light_gray_wool": (142, 142, 135),
          "lime_concrete": (94, 169, 25),
          "lime_concrete_powder": (126, 189, 42),
          "lime_terracotta": (103, 118, 53, 255),
          "lime_wool": (112, 185, 26),
          "magenta_concrete": (169, 48, 159),
          "magenta_concrete_powder": (193, 84, 185),
          "magenta_terracotta": (150, 88, 109, 255),
          "magenta_wool": (189, 69, 180),
          "orange_concrete": (224, 97, 1),
          "orange_concrete_powder": (227, 132, 32),
          "orange_terracotta": (162, 84, 38, 255),
          "orange_wool": (241, 118, 20),
          "pink_concrete": (214, 101, 143),
          "pink_concrete_powder": (229, 154, 181),
          "pink_terracotta": (162, 78, 79, 255),
          "pink_wool": (238, 141, 173),
          "purple_concrete": (100, 32, 156),
          "purple_concrete_powder": (132, 56, 178),
          "purple_terracotta": (118, 70, 86, 255),
          "purple_wool": (122, 42, 173),
          "red_concrete": (142, 33, 33),
          "red_concrete_powder": (168, 54, 51),
          "red_terracotta": (143, 61, 47, 255),
          "red_wool": (161, 39, 35),
          "terracotta": (152, 94, 68, 255),
          "white_concrete": (207, 213, 214),
          "white_concrete_powder": (226, 228, 228),
          "white_terracotta": (210, 178, 161, 255),
          "white_wool": (234, 236, 237),
          "yellow_concrete": (241, 175, 21),
          "yellow_concrete_powder": (233, 199, 55),
          "yellow_terracotta": (186, 133, 35, 255),
          "yellow_wool": (249, 198, 40)}


def main():
    disambiguation = ""
    if len(sys.argv) == 2:
        image = Image.open(sys.argv[1])
        max_pos_len = len(str(image.size[1]))+len(str(image.size[0]))
        max_mult_len = len(str(image.size[0]))
        for y in range(image.size[1])[::-1]:
            prev_block = ""
            mult = 1
            for x in range(image.size[0]):
                pixel = image.getpixel((x, y))
                sim = 195075
                sim_block = ""
                for block in blocks.keys():
                    __ = ((pixel[0] - blocks[block][0]) ** 2 + (pixel[1] - blocks[block][1]) ** 2 + (pixel[2] - blocks[block][2]) ** 2)
                    if __ < sim:
                        sim = __
                        sim_block = block
                if sim_block == prev_block:
                    mult += 1
                else:
                    if prev_block != "":
                        disambiguation += "("+str(x+1-mult)+","+str(y+1)+")"+" "*(max_pos_len-len(str(x+1-mult)+str(y+1))+1)+str(mult)+"x"+" "*(max_mult_len-len(str(mult))+1)+prev_block+"\n"
                    mult = 1
                prev_block = sim_block
                image.putpixel((x,y), blocks[sim_block])
            disambiguation += "("+str(x+1-mult+1)+","+str(y+1)+")"+" "*(max_pos_len-len(str(x+1-mult+1)+str(y+1))+1)+str(mult)+"x"+" "*(max_mult_len-len(str(mult))+1)+prev_block+"\n\n"
            image.save("pixel_art_"+sys.argv[1].split("\\")[-1])
        image.save("pixel_art_"+sys.argv[1].split("\\")[-1])
        open(".".join(sys.argv[1].split("\\")[-1].split(".")[0:-1])+"_pixel.txt","wt").write(disambiguation)
    else:
        print("Open the app by dropping the image on it")
        input("Press any key to close")

main()
