pragma solidity >=0.4.21 <0.7.0;

contract LearningContract {

    struct FileName {
        uint modelNumber;
        string fileName;
        string ipfsHash;
    }

    address public owner;
    uint public checkpointIpfsMap;
    mapping(address => FileName) public filenames;
    address[] registeredUsers;
    uint noOfRegisteredUsers;
    string checkpointIpfsHash;

    constructor () public {
        owner = msg.sender;
        noOfRegisteredUsers = 0;
    }


    function checkExistence(address testAddress) private view returns (bool) {
        for (uint i = 0; i < noOfRegisteredUsers; i++) {
            if (registeredUsers[i] == testAddress) {
                return true;
            }
        }
        return false;
    }


    function addFile(uint modelNumber, string memory fileName, string memory ipfsHash) public {

        if (!checkExistence(msg.sender)) {
            registeredUsers.push(msg.sender);
            noOfRegisteredUsers += 1;
        }

        FileName memory file;
        file.modelNumber = modelNumber;
        file.fileName = fileName;
        file.ipfsHash = ipfsHash;
        filenames[msg.sender] = file;

    }

    function getIpfsHashForUser(address user) public view returns (string memory){
        return filenames[user].ipfsHash;
    }

    function getIpfsHashForCheckpoint() public view returns (string memory){
        return checkpointIpfsHash;
    }

    function getFileNameForUser(address user) public view returns (string memory){
        return filenames[user].fileName;
    }

    function getModelNumberForUser(address user) public view returns (uint){
        return filenames[user].modelNumber;
    }

    function getRegisteredUsers(uint index) public view returns (address) {
        require(index < noOfRegisteredUsers);
        return registeredUsers[index];
    }

    function getRegisteredUsers() public view returns (address[] memory) {
        return registeredUsers;
    }

    function setCheckPointIpfsHash(string memory ipfsHash) public {
        require(msg.sender == owner);
        checkpointIpfsHash = ipfsHash;
    }

    function getCheckPointIpfsHash() public view returns(string memory) {
        return checkpointIpfsHash;
    }


}
