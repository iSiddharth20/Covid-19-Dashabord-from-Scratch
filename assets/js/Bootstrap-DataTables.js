var mSortingString = [];
var disableSortingColumn = 4;
mSortingString.push({ "bSortable": false, "aTargets": [disableSortingColumn] });

$(function() {
        var table = $('#example').dataTable({
            "paging": true,
            "ordering": false,
            "info": true,
            "aaSorting": [],
            "orderMulti": false,
            "aoColumnDefs": mSortingString

        });
});