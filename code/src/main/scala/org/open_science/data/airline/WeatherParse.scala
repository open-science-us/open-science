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

package org.open_science.data.airline

import org.open_science.data.SchemaUtils._

case class Weather( val Year   : Option[Int],
                    val Month  : Option[Int],
                    val Day    : Option[Int],
                    val TmaxF  : Option[Int],   // Max temperatur in F
                    val TminF  : Option[Int],   // Min temperatur in F
                    val TmeanF : Option[Float], // Mean temperatur in F
                    val PrcpIn : Option[Float], // Precipitation (inches)
                    val SnowIn : Option[Float], // Snow (inches)
                    val CDD    : Option[Float], // Cooling Degree Day
                    val HDD    : Option[Float], // Heating Degree Day
                    val GDD    : Option[Float]) // Growing Degree Day
//{
//  def isWrongRow():Boolean = (0 until productArity).map( idx => productElement(idx)).forall(e => e==None)
//}

object WeatherParse extends Serializable {
  implicit class WeatherImp(w: Weather) {
    def isWrongRow():Boolean = (0 until w.productArity).map( idx => w.productElement(idx)).forall(e => e==None)
  }
  
  def apply(row: Array[String]): Weather = {
    val b = if (row.length==9) 0 else 1 // base index
    val d = parseDate(row(b)).getOrElse( (None, None, None) )
    
    Weather(d._1, d._2, d._3,
            int  (row(b + 1)),
            int  (row(b + 2)),
            float(row(b + 3)),
            float(row(b + 4)),
            float(row(b + 5)),
            float(row(b + 6)),
            float(row(b + 7)),
            float(row(b + 8))
    )
  }
}