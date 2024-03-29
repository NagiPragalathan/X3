// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DataStorage {
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
    
    mapping(address => Data) userData;
    mapping(uint256 => Data) idData;

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
        string memory _resultValue
    ) public {
        address userAddress = msg.sender;
        userData[userAddress] = Data(_lex, _tokens, _fullCode, _ast, _parser, _result, _context, _symbolTable, _executionTime, _resultValue);
    }
    function senderAddress()returns address{
        return msg.sender
    }

    function setDataById(
        uint256 _id,
        string memory _lex,
        string memory _tokens,
        string memory _fullCode,
        string memory _ast,
        string memory _parser,
        string memory _result,
        string memory _context,
        string memory _symbolTable,
        uint256 _executionTime,
        string memory _resultValue
    ) public {
        idData[_id] = Data(_lex, _tokens, _fullCode, _ast, _parser, _result, _context, _symbolTable, _executionTime, _resultValue);
    }

    function getDataByAddress(address _userAddress) public view returns (Data memory) {
        return userData[_userAddress];
    }

    function getDataById(uint256 _id) public view returns (Data memory) {
        return idData[_id];
    }
}
