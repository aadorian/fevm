const MinerAPI = artifacts.require("MinerAPI");

module.exports = function(deployer) {
  deployer.deploy(MinerAPI,'MinerAPI');

};