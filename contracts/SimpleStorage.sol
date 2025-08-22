// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract SimpleStorage {
    uint256 private value;

    event ValueChanged(uint256 newValue);

    function set(uint256 _v) external {
        value = _v;
        emit ValueChanged(_v);
    }

    function get() external view returns (uint256) {
        return value;
    }
}
