

## GIT repo 

## Video 

### Usefull commands
![](https://i.imgur.com/NrQRoYS.png)

- [x] npm install truffle
- [x] ./node_modules/.bin/truffle init
- [x] ./node_modules/.bin/truffle compile
- [x] ./node_modules/.bin/truffle develop --log
> - [x] ./node_modules/.bin/truffle migrate (tested but not working on FEVM)

```javascript
web3
web3.currentProvider
web3.eth.getBalance('0x..')

let accounts = await web3.eth.getAccounts()
accounts
networks

let instance = await Storage.deployed()
instance.store(1, {from: accounts[0]})
instance.retrieve( {from: accounts[0]})
let balance = await instance.getBalance(accounts[0])
let newInstance = await Storage.new()
newInstance.address


```

## Dependencies

```json
{
  "scripts": {
    "start": "streamlit run main.py"
  },
  "dependencies": {
    "@truffle/hdwallet-provider": "^2.1.1",
    "dotenv": "^16.0.3",
    "truffle": "^5.6.6"
  },
  "devDependencies": {
    "truffle-plugin-verify": "^0.6.0"
  }
}

```
## Tested

>npm install @openzeppelin/contracts
>npx truffle migrate --network development
>./node_modules/.bin/truffle deploy --development
>./node_modules/.bin/truffle  migrate --network live

## Deployed

'Storage'
   -------------------
   > transaction hash:    0xeac75f675a9bbcc108643b88a9e71b6a4c6bcd1fb29afa2c78963950149d69cd
   > Blocks: 3            Seconds: 71
   > contract address:    0x0ad82D84073CC34b689cB74ceb6759a61D4e58fe
   > block number:        5036
   > block timestamp:     1668837407
   > account:             0x164E5bcfd03114121695a207A114B1b589c8534B
   > balance:             4999.8688395735154476
   > gas used:            33584870 (0x20076e6)
   > gas price:           0 gwei
   > value sent:          0 ETH
   > total cost:          0 ETH


   https://explorer.glif.io/tx/0xeac75f675a9bbcc108643b88a9e71b6a4c6bcd1fb29afa2c78963950149d69cd/?network=wallaby


##  Not working en FEVM
npm install -D truffle-plugin-verify

## Configuration to deploy live
> truffle-config.js file
   live: {
      network_id: 18, 
      provider:   new HDWalletProvider(MNEMONIC, `https://wallaby.node.glif.io/rpc/v0`),

    },

### Resources



https://docs.zondax.ch/Beryx
https://web3-tools.netlify.app/
https://trufflesuite.com

#### Prices

https://ethglobal.com/events/hackfevm/prizes 
https://github.com/filecoin-project/FEVM-Hardhat-Kit/tree/main/contracts/filecoinMockAPIs

## Snapshots
![](https://i.imgur.com/OiLdCB8.png)


```

```
0x0AD82D84073CC34B689CB74CEB6759A61D4E58fE

0xde6b3c5c8a621b5e29afcabcfbba0243f3a3b5ab37fc1d3b2e0dff737616baf8

![](https://i.imgur.com/wwRdmmA.png)
![](https://i.imgur.com/PglWkbO.png)


`t410fq5bq6eh23g44xbafni37qnwyvaccaqydncmf2ea`




python -m pip install -r requirements.txt