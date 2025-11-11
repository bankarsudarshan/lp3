// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {
    // structure
    struct Student{
        string name;
        uint256 rollno;
        string class;
        uint256 age;
    }

    // arrays
    Student[] public studentArr;

    function addStudent(string memory name, uint256 rollno, string memory class, uint256 age) public{
        for(uint i=0; i<studentArr.length; i++) {
            if(studentArr[i].rollno == rollno)
                revert("Student with this roll number already exists");
        }

        studentArr.push(Student(name, rollno, class, age));
    }

    function getStudentLength() public view returns(uint) {
        return studentArr.length;
    }

    function displayAllStudents() public view returns(Student[] memory) {
        return studentArr;
    }

    function getStudentByRollNo(uint rollno) public view returns(Student memory) {
        for(uint i=0; i<studentArr.length; i++) {
            if(studentArr[i].rollno == rollno)
                return studentArr[i]; 
        }

        revert("Student not found");
    }

    fallback() external payable { 
        // This function will handle external function calls that are not in contract
    }

    receive() external payable { 
        // This function will handle ether sent by external user but without data mentioned
    }
}
