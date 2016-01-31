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

// Airline can not be case class because the 22 limitation
class Airline (
                val Year              : Option[Int],
                val Month             : Option[Int],
                val DayofMonth        : Option[Int],
                val DayOfWeek         : Option[Int],
                val DepTime           : Option[Int],
                val CRSDepTime        : Option[Int],
                val ArrTime           : Option[Int],
                val CRSArrTime        : Option[Int],
                val UniqueCarrier     : Option[String],
                val FlightNum         : Option[Int],
                val TailNum           : Option[String],
                val ActualElapsedTime : Option[Int],
                val CRSElapsedTime    : Option[Int],
                val AirTime           : Option[Int],
                val ArrDelay          : Option[Int],
                val DepDelay          : Option[Int],
                val Origin            : Option[String],
                val Dest              : Option[String],
                val Distance          : Option[Int],
                val TaxiIn            : Option[Int],
                val TaxiOut           : Option[Int],
                val Cancelled         : Option[Int],
                val CancellationCode  : Option[Int],
                val Diverted          : Option[Int],
                val CarrierDelay      : Option[Int],
                val WeatherDelay      : Option[Int],
                val NASDelay          : Option[Int],
                val SecurityDelay     : Option[Int],
                val LateAircraftDelay : Option[Int],
                val IsArrDelayed      : Option[Boolean],
                val IsDepDelayed      : Option[Boolean]) extends Product with Serializable {
  override def canEqual(that: Any):Boolean = that.isInstanceOf[Airline]
  override def productArity: Int = 31
  override def productElement(n: Int) = n match {
    case  0 => Year
    case  1 => Month
    case  2 => DayofMonth
    case  3 => DayOfWeek
    case  4 => DepTime
    case  5 => CRSDepTime
    case  6 => ArrTime
    case  7 => CRSArrTime
    case  8 => UniqueCarrier
    case  9 => FlightNum
    case 10 => TailNum
    case 11 => ActualElapsedTime
    case 12 => CRSElapsedTime
    case 13 => AirTime
    case 14 => ArrDelay
    case 15 => DepDelay
    case 16 => Origin
    case 17 => Dest
    case 18 => Distance
    case 19 => TaxiIn
    case 20 => TaxiOut
    case 21 => Cancelled
    case 22 => CancellationCode
    case 23 => Diverted
    case 24 => CarrierDelay
    case 25 => WeatherDelay
    case 26 => NASDelay
    case 27 => SecurityDelay
    case 28 => LateAircraftDelay
    case 29 => IsArrDelayed
    case 30 => IsDepDelayed
    case  _ => throw new IndexOutOfBoundsException(n.toString)
  }
  
  override def toString:String = {
    val sb = new StringBuffer("Airline(")
    
    for( i <- 0 until productArity )
      sb.append(productElement(i)).append(',')
    
    sb.setLength(sb.length() - 1);
    sb.append(')')
    
    sb.toString
  }

  def isWrongRow():Boolean = {
    // val b = (0 until productArity).map(idx => productElement(idx)).forall(e => e == None)   
    // val d = (0 to 3).map(idx => productElement(idx)).forall(e => e != None)
    (0 until productArity).map(idx => productElement(idx)).forall(e => e == None) | !(0 to 3).map(idx => productElement(idx)).forall(e => e != None)
  }
}

object AirlineParse extends Serializable {  
  def apply(row: Array[String]): Airline = {
    new Airline(
      int (row( 0)), // Year
      int (row( 1)), // Month
      int (row( 2)), // DayofMonth
      int (row( 3)), // DayOfWeek
      int (row( 4)), // DepTime
      int (row( 5)), // CRSDepTime
      int (row( 6)), // ArrTime
      int (row( 7)), // CRSArrTime
      str (row( 8)), // UniqueCarrier
      int (row( 9)), // FlightNum
      str (row(10)), // TailNum
      int (row(11)), // ActualElapsedTime
      int (row(12)), // CRSElapsedTime
      int (row(13)), // AirTime
      int (row(14)), // ArrDelay
      int (row(15)), // DepDelay
      str (row(16)), // Origin
      str (row(17)), // Dest
      int (row(18)), // Distance
      int (row(19)), // TaxiIn
      int (row(20)), // TaxiOut
      int (row(21)), // Cancelled
      int (row(22)), // CancellationCode
      int (row(23)), // Diverted
      int (row(24)), // CarrierDelay
      int (row(25)), // WeatherDelay
      int (row(26)), // NASDelay
      int (row(27)), // SecurityDelay
      int (row(28)), // LateAircraftDelay
      bool(row(29)), // IsArrDelayed
      bool(row(30))) // IsDepDelayed
  }
}