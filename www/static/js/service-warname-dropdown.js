var data = [{"code" : "0001", "name" : "CC", 
                            "warname" : [{"code" : "00010001", "name" : "call-web.war"},
                                        {"code" : "00010002", "name" : "cc-report-web.war"},
                                        {"code" : "00010003", "name" : "ccStaticResources-web.war"},
                                        {"code" : "00010004", "name" : "cc-sync-web.war"},
                                        {"code" : "00010005", "name" : "DepponOrderSelect.war"},
                                        {"code" : "00010006", "name" : "job-web.war"},
                                        {"code" : "00010007", "name" : "solr.war"}]},
            {"code" : "0002", "name" : "CRM", 
                            "warname" : [{"code" : "00020001", "name" : "crm.war"},
                                        {"code" : "00020002", "name" : "crm-agiledev.war"},
                                        {"code" : "00020003", "name" : "crm-cache.war"},
                                        {"code" : "00020004", "name" : "crm-mobileinterface.war"},
                                        {"code" : "00020005", "name" : "crm-report.war"},
                                        {"code" : "00020006", "name" : "crm-reportScheduler.war"},
                                        {"code" : "00020007", "name" : "crm-scheduler.war"},
                                        {"code" : "00020008", "name" : "crm-web.war"},
                                        {"code" : "00020009", "name" : "job.war"}]}];

window.onload = function(){
    // 获取服务名select
    var proSelect = document.getElementById("service");
    for (var i = 0; i < data.length; i++)
    {
        var json = data[i];
        var option = new Option(json.name, json.code, false, false);
        proSelect.add(option);
    }
    // 为proSelect绑定onChange事件
    proSelect.onchange = function(){
        
        var citySelect = document.getElementById("warname");
        // 在下次选择服务之前先清空war包名下拉列表
        for (var i = citySelect.length - 1; i > 0; i--)
        {
            citySelect.remove(i);
        }
        for (var i = 0; i < data.length; i++)
        {
            var json = data[i];
            if (json.code == this.value)
            {
                // 取城市
                var warname = json.warname;
                for (var j = 0; j < warname.length; j++)
                {
                    // 获取其中的json
                    var temp = warname[j];
                    var option = new Option(temp.name, temp.code, false, false);
                    citySelect.add(option);
                }
            }
        }
    };
};