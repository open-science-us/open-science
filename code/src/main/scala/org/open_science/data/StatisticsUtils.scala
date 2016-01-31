package org.open_science.data

object StatisticsUtils {
    def median(xs: Seq[Double]): Double = {
    if (xs.size % 2 == 0) (xs(xs.size / 2 - 1) + xs(xs.size / 2)) / 2
    else xs(xs.size / 2)
  }

  def iqr(xs: Seq[Double]): Double = {
    if (xs.size % 4 == 0) (xs(xs.size * 3 / 4 - 1) + xs(xs.size * 3 / 4)) / 2 - (xs(xs.size / 4 - 1) + xs(xs.size / 4)) / 2
    else if (xs.size % 2 == 0 || xs.size % 4 == 1) xs(xs.size * 3 / 4) - xs(xs.size / 4)
    else (xs(xs.size * 3 / 4 - 1) + xs(xs.size * 3 / 4)) / 2 - (xs(xs.size / 4 + 1) + xs(xs.size / 4)) / 2
  }

  def mean(xs: Seq[Double]): Double = {
    xs.reduce(_ + _) / xs.size
  }
}