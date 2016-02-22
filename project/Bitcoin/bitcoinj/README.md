## [bitcoinj](https://bitcoinj.github.io)

### Using bitcoinj with Scala

#### Creating an Address
~~~
import org.bitcoinj.core.NetworkParameters
import org.bitcoinj.core.Address
import org.bitcoinj.core.ECKey
import org.bitcoinj.params._

import org.bitcoinj.utils.BriefLogFormatter


object CreatingAddress {
  def main(args: Array[String]) {
    BriefLogFormatter.init();
    
    if (args.length != 1) {
        System.err.println("Usage: CreatingAddress [regtest|testnet]");
        return;
    }
    
    var params: NetworkParameters = null
    
    if (args(0) == "testnet") {
      params = TestNet3Params.get()
    } else if (args(0) == "regtest") {
      params = RegTestParams.get()
    } else {
      params = MainNetParams.get()
    }
    
    val key = new ECKey()
    println("We created key:\n" + key)
    
    val addressFromKey = key.toAddress(params);
    println("On the " + args(0) + " network, we can use this address:\n" + addressFromKey);    
  }
}
~~~
