from PIL import Image
from scipy import stats
from scipy.stats import pearsonr
import scipy.misc
from scipy import ndimage
from imageio import imsave
import matplotlib.pyplot as plt



def main():

    # 二項検定
    # ひずみのないサイコロかどうか？
    # print(stats.binom_test(1050, 6000, 1/6))

    # 優位水準5％として結果を判断
    # P値

    # 相関関数
    # usdjpy = [101.98, 101.85, 102.34, 102.23, 102.33]
    # eurjpy = [101.98, 101.85, 102.15, 102.11, 102.33]
    # print(stats.pearsonr(usdjpy, eurjpy))

    face = scipy.misc.face()
    plt.imsave('face.png', face)

    rotate_face = ndimage.rotate(face, 45)
    plt.imsave('rotate_face.jpg', rotate_face)






    return


if __name__ == "__main__":

    main()