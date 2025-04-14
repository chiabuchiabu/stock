document.addEventListener("DOMContentLoaded",function(){

    const ctx=document.getElementById('mychart').getContext('2d');
    const myChart=new Chart(ctx,{
        type:'bar',
        data:{
            labels:chartLabels,
            datasets:[{
                label:' 淨利 Net Income (美元）',
                data:chartValues,
                backgroundColor:'rgba(75,192,192,0.5)'
            }]},

    })
})
