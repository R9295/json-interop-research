const assert = require('assert');

const assert_dict = (a, b) => {
    try {
        assert.deepStrictEqual(a, b);
        return true;
    } catch (error) {
        return false
    }
}

const assert_list = (a, b) => {
    try {
        assert.deepStrictEqual(a, b);
        return true;
    } catch (error) {
        return false
    }
}

const assert_float = (a, b) => {
    return (
        typeof a === "number" && !Number.isInteger(a) && !Number.isInteger(b) && a === b
    )
}

const assert_str = (a, b) => {
    return typeof a === 'string' && a === b
}

const assert_bool = (a, b) => {
    return typeof a === 'boolean' && a === b
}

const assert_int = (a, b) => {
    return (
        typeof a === 'number' && Number.isInteger(a) && a === b
    )
}

const assert_none = (a, b) => {
    return a === null && b === null
}

exports.assert_str = assert_str
exports.assert_float = assert_float
exports.assert_list = assert_list
exports.assert_dict = assert_dict
exports.assert_none = assert_none
exports.assert_int = assert_int
exports.assert_bool = assert_bool
