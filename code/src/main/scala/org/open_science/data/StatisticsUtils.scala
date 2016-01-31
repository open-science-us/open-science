/*
* Licensed to the Apache Software Foundation (ASF) under one or more
* contributor license agreements.  See the NOTICE file distributed with
* this work for additional information regarding copyright ownership.
* The ASF licenses this file to You under the Apache License, Version 2.0
* (the "License"); you may not use this file except in compliance with
* the License.  You may obtain a copy of the License at
*
*    http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*/


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