// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

/**
 * @title Storage
 * @dev Store & retrieve value in a variable
 * @custom:dev-run-script ./scripts/deploy_with_ethers.ts
 */
contract Storage {

    uint256 number;
    string metadata;

    /**
     * @dev Store value in variable
     * @param num value to store
     */
    function store(uint256 num) public {
        number = num;
    }

    /**
     * @dev Return value 
     * @return value of 'number'
     */
    function retrieve() public view returns (uint256){
        return number;
    }
    /**
     * @dev Store value in variable
     * @param _metadata value to store
     */
    function storeMetadata(string memory _metadata) public {
        metadata = _metadata;
    }   
    /**
     * @dev Return value 
     * @return value of 'metadata'
     */
    function retrieveMetadata() public view returns (string memory){
        return metadata;
    }
    
}