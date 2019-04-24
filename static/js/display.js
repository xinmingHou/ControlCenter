// 在ready方法表示文档加载后激活
$(document).ready(function(){
    $("#uploadfile").fileinput({

                language: 'zh', //设置语言

                uploadUrl:"http://127.0.0.1/fileupload/", //上传的地址

                allowedFileExtensions: ['py', 'h5', 'ipynb'],//接收的文件后缀

                //uploadExtraData:{"id": 1, "fileName":'123.mp3'},

                uploadAsync: true, //默认异步上传

                showUpload:true, //是否显示上传按钮

                showRemove :true, //显示移除按钮

                showPreview :true, //是否显示预览

                showCaption:true,//是否显示标题

                browseClass:"btn btn-primary", //按钮样式    

                dropZoneEnabled: true,//是否显示拖拽区域

                minImageWidth: 50, //图片的最小宽度

                minImageHeight: 50,//图片的最小高度

                maxImageWidth: 1000,//图片的最大宽度

                maxImageHeight: 1000,//图片的最大高度

                maxFileSize:0,//单位为kb，如果为0表示不限制文件大小

                minFileCount: 0,

                maxFileCount:10, //表示允许同时上传的最大文件个数

                enctype:'multipart/form-data',

                validateInitialCount:true,

                previewFileIcon: "<iclass='glyphicon glyphicon-king'></i>",

                msgFilesTooMany: "选择上传的文件数量({n}) 超过允许的最大数值{m}！",

           }).on("fileuploaded", function (event, data, previewId, index){
    });
    
    $('body').scrollspy({ target: '#navbar-docs' });    
   
    $("#submit_job").click(function(){
        var jobname =  $("#jobname").val(); // 获取jobname
        var gpus = $("#gpus").val();
        console.log("submit");
        var data = {"jobname": jobname,
                    "gpus":gpus,
                };  // 打包成get请求发送的数据
        $.ajax({
            // 请求的url,记录在路由表里
            url : '/submit_job/',
            // 发送的数据
            type:'POST',
            data:data,
            // 回调函数，其中ret是返回的JSON，可以以字典的方式调用
            success:function(ret){
                console.log(ret);
                console.log("ok");
            }
        })
    })

 




})

function selected_temp(element){
    console.log(element.id);
    var name_templ = element.id;
    var d = {"name_templ": name_templ};  // 打包成get请求发送的数据
    $.ajax({
        // 请求的url,记录在路由表里
        url : '/copy_tem/',
        // 发送的数据
        type:'GET',
        data:d,
        // 回调函数，其中ret是返回的JSON，可以以字典的方式调用
        success:function(ret){
            console.log(ret)

            location.href = "/ide_editor/"

        }
    })



};










   


