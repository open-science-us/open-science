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

package org.open_science.clustering

import java.lang.Math._
import scala.util.control._

object Neighbor {
  def distance(xs: Seq[Double]): Array[Array[(Int, Double)]] = {
    val ds = distanceImpl(xs)
    
    for (i <- 0 until ds.size) {
      val sm = ds(i).sortBy(t => t._2)
      
      for (j<- 0 until ds(i).size) {
        ds(i)(j) = sm(j)
      }
    }
    
    ds
  }

  def knn(xs: Seq[Double], k: Int): Array[Array[(Int, Double)]] = {    
    knnImpl(distanceImpl(xs), k)
  }
  
  def lof(xs: Seq[Double], k: Int):  Array[Double] = {
    val ds = distanceImpl(xs)
    
    val knn = knnImpl(ds, k)
    
    val lrds = lrdImpl(ds, knn, k)
    
    val lofs = new Array[Double](xs.size)
    
    for (i <- 0 until lrds.size) {
      var ls = 0.0
      
      for (j <- 0 until k) {
        ls += lrds(knn(i)(j)._1)
      }
      
      lofs(i) = ls / k / lrds(i)
    }
    
    lofs
  }
  
  // get rid of duplicated points
  def lof2(xs: Seq[Double], k: Int):  Array[Double] = {
    val ds = distanceImpl(xs)
    
    val knn = knnImpl(ds, k)
    
    val lrds = lrdImpl(ds, knn, k)
    
    val lofs = new Array[Double](xs.size)
    
    for (i <- 0 until xs.size) {
      var ls = 0.0
      
      for (j <- 0 until k) {
        ls += lrds(knn(i)(j)._1)
      }
      
      lofs(i) = ls / k / lrds(i)
    }
    
    lofs
  }
  
  
  private def distanceImpl(xs: Seq[Double]): Array[Array[(Int, Double)]] = {
    val ds = Array.ofDim[(Int, Double)](xs.size, xs.size)
    
    for (i <- 0 until xs.size; j<- 0 until xs.size) {
      ds(i)(j) = (j, abs(xs(i) - xs(j)))
    }
    
    ds
  }
   
  private def knnImpl(ds: Array[Array[(Int, Double)]], k: Int): Array[Array[(Int, Double)]] = {
    val knn = Array.ofDim[(Int, Double)](ds.length, k)
    
    for (i <- 0 until ds.length) {
      val sm = ds(i).sortBy(t => t._2)  
      
      var z0 = 0;
      while (sm(z0)._2 == 0 & z0 < ds.length) z0 = z0 + 1
      
      var max = 0.0
      for (j <- 0 until k) {
        if ((z0+j) < ds.length) {
          knn(i)(j) = sm(z0+j)
          max = sm(z0+j)._2
        } else knn(i)(j) = (i, max)
      }
    }
    
    knn
  }
  
  private def lrdImpl(ds: Array[Array[(Int, Double)]], knn: Array[Array[(Int, Double)]], k: Int): Array[Double] = {
    val lrds = new Array[Double](ds.length)
    
    for (i <- 0 until ds.length) {
      var rd = 0.0
      var count = 0
      
      for (j <- 0 until k) {
        var b = knn(i)(j)._1
        
        if (b != i) {
          count = count + 1
          if (knn(b)(k-1)._2 > ds(i)(b)._2) rd += knn(b)(k-1)._2
          else rd += ds(i)(b)._2
        }
      }
      
      if (count == 0 || rd == 0.0) lrds(i) = 0.0
      else lrds(i) = count / rd
    }

    lrds
  }
  
  private def normalizeLOF(lofs: Array[Double]): Array[Double] = {
    var minLof = 0.0; var maxLof = 0.0
    
    for (i <- 0 until lofs.length) {      
      if (lofs(i) < minLof) minLof = lofs(i)
      else if (lofs(i) > maxLof) maxLof = lofs(i)
    }
    
    if (maxLof == minLof) {
      for (i <- 0 until lofs.length) {
        lofs(i) = 0.0
      }
    } else {
      for (i <- 0 until lofs.length) {
        lofs(i) = lofs(i) / (maxLof - minLof)
      }
    }
    
    lofs
  }
  
  def lof3(xs: Seq[Double], k: Int):  Array[Double] = {
    if (xs.size <= k) {
      val lofs = new Array[Double](xs.size)
      
      for (i <- 0 until xs.size) lofs(i) = 0.0
      
      return lofs
    }
    
    val ds = distanceImpl(xs)
    
    val knn = knnImpl(ds, k)
    
    val lrds = lrdImpl(ds, knn, k)
    
    val lofs = new Array[Double](xs.size)
    
    for (i <- 0 until xs.size) {
      var ls = 0.0
      
      for (j <- 0 until k) {
        ls += lrds(knn(i)(j)._1)
      }
      
      lofs(i) = ls / k / lrds(i)
    }

    normalizeLOF(lofs)
  }
}