// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/utils/Counters.sol";

contract DataStorage {
    using Counters for Counters.Counter;
    Counters.Counter private _dataIdCounter;

    struct Data {
        string lex;
        string tokens;
        string fullCode;
        string ast;
        string parser;
        string result;
        string context;
        string symbolTable;
        uint256 executionTime;
        string resultValue;
    }
    
    mapping(address => Data[]) userData; // Mapping from user address to an array of Data
    mapping(uint256 => Data[]) idData; // Mapping from ID to an array of Data

    function setData(
        string memory _lex,
        string memory _tokens,
        string memory _fullCode,
        string memory _ast,
        string memory _parser,
        string memory _result,
        string memory _context,
        string memory _symbolTable,
        uint256 _executionTime,
        string memory _resultValue,
        address user_address
    ) public {
        uint256 newId = _dataIdCounter.current();
        _dataIdCounter.increment();

        Data memory newData = Data(_lex, _tokens, _fullCode, _ast, _parser, _result, _context, _symbolTable, _executionTime, _resultValue);
        
        // Push new data to the array for the new ID
        idData[newId].push(newData);
        
        // Push new data to the array for the sender's address
        userData[user_address].push(newData);
    }

    function getDataByAddress(address _userAddress) public view returns (Data[] memory) {
        return userData[_userAddress];
    }

    function getDataById(uint256 _id) public view returns (Data[] memory) {
        require(_id < _dataIdCounter.current(), "ID does not exist.");
        return idData[_id];
    }
}