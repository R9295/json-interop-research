const fs = require('fs');

const getModuleName = (path) => {
    return path.split('/').at(-2).replace('_tests', '')
}

const getFileName = (path) => {
    return path.split('/').at(-1).replace('.test.js', '')
}

class Reporter {
    onRunComplete(context, results) {
        const parsedResults = {}
        results.testResults.forEach(file => {
            const test_arr = file.testResults
            const parsed_test_results = []
            const moduleName = getModuleName(file.testFilePath)
            const fileName = getFileName(file.testFilePath)
            test_arr.forEach(test => {
                parsed_test_results.push(
                    {
                        'name': `${fileName}::${test.title}`,
                        'result': `${test.status}`
                    }
                )
            })
            try { 
                parsedResults[moduleName] = parsedResults[moduleName].concat(parsed_test_results)
            } catch (error) {
                parsedResults[moduleName] = parsed_test_results
            }
        });
        fs.writeFileSync('./report.json', JSON.stringify(parsedResults, null, '\t'))
    }
}

module.exports = Reporter
