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
    
    wallet.importKey(new ECKey());
    wallet.importKey(new ECKey());
    wallet.importKey(new ECKey());
    
    val walletFile = new File("/work/bitcoinj/" + args(0) + ".wallet")
    
    wallet.saveToFile(walletFile);   
  }
}
~~~

Output
~~~
$ ls -al /work/bitcoinj/testnet.wallet

-rw-r--r--  1 scheng  staff  900 Feb 22 11:30 /work/bitcoinj/testnet.wallet
~~~


### Checking the Wallet
~~~
import java.io.File

import org.bitcoinj.core.NetworkParameters
import org.bitcoinj.core.Address
import org.bitcoinj.core.ECKey
import org.bitcoinj.core.Wallet
import org.bitcoinj.wallet.KeyChain
import org.bitcoinj.params._

import org.bitcoinj.utils.BriefLogFormatter


object CheckingWallet {
  def main(args: Array[String]) {
    BriefLogFormatter.init();
    
    if (args.length != 1) {
        System.err.println("Usage: CheckingWallet [regtest|testnet|production]");
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
      System.err.println("Usage: CheckingWallet [regtest|testnet|production]");
      return;
    }
    
    val walletFile = new File("/work/bitcoinj/" + args(0) + ".wallet")
    
    val wallet = Wallet.loadFromFile(walletFile)
    
    val key = wallet.getActiveKeychain.getKey(KeyChain.KeyPurpose.RECEIVE_FUNDS)
    println("key in the wallet:\n" + key)
    
    println("Complete content of the wallet:\n" + wallet)
   
    if (wallet.isPubKeyHashMine(key.getPubKeyHash())) {
      println("Yep, that's my key.")
    } else {
      println("Nope, that key didn't come from this wallet.")
    }
  }
}
~~~

Output
~~~
key in the wallet:
DeterministicKey{pub=0217f22220157dabcf3d907a223e9cf9550652ef5bea5f8d6a09b2ee618e403d9d, chainCode=66a99dd2e4ab1003e48264aa218e6db571bb2201b1340059ad0e75a347898aeb, path=M/0H/0/0, isEncrypted=false, isPubKeyOnly=false}
Complete content of the wallet:
Wallet containing 0 BTC (spendable: 0 BTC) in:
  0 pending transactions
  0 unspent transactions
  0 spent transactions
  0 dead transactions
Last seen best block: -1 (time unknown): null

Keys:
  addr:mmpDJ5wieUrWHLjzSQnRa66xaxPYWU8zTy  hash160:4514590ee3de35e5449d856a8a1f1da6f37afa66  creationTimeSeconds:1456158639
  addr:mqFaFJEnkK7BsnGBjrvVG6v5Lx1oZNg5FA  hash160:6ac89d33b6ebed212fcc2c8dae3f5bb7909b1777  creationTimeSeconds:1456158639
  addr:mqNFKs1gJituA79U3XUHaHNF3PyVrEbRk1  hash160:6c0bbb299e2d04040667f12183eba236c9b41af4  creationTimeSeconds:1456158639
Seed birthday: 1456158638  [2016-02-22T16:30:38Z]
Key to watch:  tpubD8PV1e3sSciaKx9eBRmzgkCcFLRRDH4En35bQqe5ZZE1wnv9PasB3jxNCUdBjmvVp2sSVJDMwwE7ocsP49HfbEo2fw4RMKV5Vwup9tKB1d8
  addr:mnVhNh1GzRzXFgSPAeW2cMoq6WdvRXmXXN  hash160:4c8c0287e2e6b6a6f1ba7b04957d8abc1bb120fe  (M/0H/0/0)

Yep, that's my key.
~~~


### Fetching the Genesis Block
~~~
import java.io.File
import java.io.IOException
import java.net.InetAddress
import java.net.UnknownHostException

import scala.collection.JavaConversions._

import org.bitcoinj.core.NetworkParameters
import org.bitcoinj.core.Block
import org.bitcoinj.core.BlockChain
import org.bitcoinj.core.Wallet
import org.bitcoinj.core.PeerGroup
import org.bitcoinj.core.Peer
import org.bitcoinj.core.PeerAddress
import org.bitcoinj.net.discovery.DnsDiscovery
import org.bitcoinj.core.AbstractPeerEventListener
import org.bitcoinj.core.Sha256Hash
import org.bitcoinj.store.BlockStore
import org.bitcoinj.store.BlockStoreException
import org.bitcoinj.store.MemoryBlockStore
import org.bitcoinj.params._

import org.bitcoinj.utils.BriefLogFormatter


object FetchingGenesisBlock {
  def main(args: Array[String]) {
    BriefLogFormatter.init();
    
    if (args.length != 1) {
        System.err.println("Usage: FetchingGenesisBlock [regtest|testnet|production]");
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
      System.err.println("Usage: FetchingGenesisBlock [regtest|testnet|production]");
      return;
    }

        
    val blockStore = new MemoryBlockStore(params)
    val blockChain = new BlockChain(params, blockStore)
    val peerGroup = new PeerGroup(params, blockChain)
    
    peerGroup.setUserAgent("Sample App", "1.0")
    peerGroup.addAddress(new PeerAddress(InetAddress.getLocalHost(), 8333))
    
    val walletFile = new File("/work/bitcoinj/" + args(0) + ".wallet")
    val wallet = Wallet.loadFromFile(walletFile)
    peerGroup.addWallet(wallet)
    
    peerGroup.addPeerDiscovery(new DnsDiscovery(params))
    
    peerGroup.start
    println("PeerGroup is running? " + peerGroup.isRunning()) 
    
    println("START DOWNLOADING BLOCKCHAIN")
    val start = System.currentTimeMillis
    peerGroup.downloadBlockChain()
    println("DOWNLOADING BLOCKCHAIN takes " + (System.currentTimeMillis - start) / 1000 + " seconds.")
    
    
    val peers = peerGroup.getConnectedPeers 
    println("number of connected peers: " + peers.size)
    
    peers.foreach { println }
    
    
    val peer = peerGroup.getDownloadPeer
    
    val blockFuture = peer.getBlock(new Sha256Hash("000000000933ea01ad0ee984209779baaec3ced90fa3f408719526f8d77f4943"))
    
    val block = blockFuture.get
    println("Here is the genesis block:\n" + block);
    
    
    peerGroup.stop    
    println("DONE; BALANCE IS :" + wallet.getBalance)
  }
}
~~~

Output
~~~
PeerGroup is running? true
START DOWNLOADING BLOCKCHAIN
DOWNLOADING BLOCKCHAIN takes 61 seconds.
number of connected peers: 1
[52.1.165.219]:18333
Here is the genesis block:
v1 block: 
   previous block: 0000000000000000000000000000000000000000000000000000000000000000
   merkle root: 4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b
   time: [1296688602] 2011-02-02T23:16:42Z
   difficulty target (nBits): 486604799
   nonce: 414098458
   with 1 transaction(s):
  4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b: Unknown confidence level.
     == COINBASE TXN (scriptSig PUSHDATA(4)[ffff001d] PUSHDATA(1)[04] PUSHDATA(69)[5468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73])  (scriptPubKey PUSHDATA(65)[04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f] CHECKSIG)

DONE; BALANCE IS :0
~~~
