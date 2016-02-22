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

Output
~~~
We created key:
ECKey{pub HEX=033299e4d8f016545263172422779a33d6682a3efa17082051a8d00670eee15076, creationTimeSeconds=1456155057, isEncrypted=false, isPubKeyOnly=false}
On the testnet network, we can use this address:
n3Xi9VVU58sEy4tku2qCf76nvzgMoFYhd6
~~~


### Creating a Wallet
~~~
import java.io.File

import org.bitcoinj.core.NetworkParameters
import org.bitcoinj.core.Address
import org.bitcoinj.core.ECKey
import org.bitcoinj.core.Wallet
import org.bitcoinj.params._

import org.bitcoinj.utils.BriefLogFormatter


object CreatingWallet {
  def main(args: Array[String]) {
    BriefLogFormatter.init();
    
    if (args.length != 1) {
        System.err.println("Usage: CreatingWallet [regtest|testnet|production]");
        return;
    }
    
    var params: NetworkParameters = null
    
    if (args(0) == "testnet") {
      params = TestNet3Params.get()
    } else if (args(0) == "regtest") {
      params = RegTestParams.get()
    } else if (args(0) == "production") {
      params = MainNetParams.get()
    } else {
      System.err.println("Usage: CreatingWallet [regtest|testnet|production]");
      return;
    }
    
    val wallet = new Wallet(params)
    
    wallet.addKey(new ECKey());
    wallet.addKey(new ECKey());
    wallet.addKey(new ECKey());
    
    val walletFile = new File("/work/bitcoinj/" + args(0) + ".wallet")
    
    wallet.saveToFile(walletFile);   
  }
}
~~~
