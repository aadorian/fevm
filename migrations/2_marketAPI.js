const MarketAPI = artifacts.require("MarketAPI");

module.exports = function(deployer) {
  deployer.deploy(MarketAPI);

};