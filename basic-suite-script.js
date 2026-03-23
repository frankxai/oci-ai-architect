/**
 * @NApiVersion 2.x
 * @NScriptType UserEventScript
 */
define(['N/record', 'N/log'], function(record, log) {

    function beforeLoad(context) {
        log.debug('Basic SuiteScript', 'Record ID: ' + context.newRecord.id);
    }

    function beforeSubmit(context) {
        // No action in this basic example
    }

    function afterSubmit(context) {
        // No action in this basic example
    }

    return {
        beforeLoad: beforeLoad,
        beforeSubmit: beforeSubmit,
        afterSubmit: afterSubmit
    };
});