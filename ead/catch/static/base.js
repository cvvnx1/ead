function getData(handlePage,appendObj,inputData){
  $.ajax({
    type: 'POST',
    async: true,
    url: handlePage,
    data: inputData,
    dataType: 'json',
    beforeSend:function(){
      process_bar(true);
    },
    success:function(data){
      process_bar(false);
      process_list(data);
    },
    error:function(){
      $("div#process_bar").text('ebay connect error!');
    }
  });
}

function sellItem(handlePage,inputData){
  $.ajax({
    type: 'POST',
    async: true,
    url: handlePage,
    data: inputData,
    dataType: 'json',
    success:function(data){
      $("div#sell_itemid").html('Last sold ItemID: <a href="' + data.link + '" target="_blank" >' + data.itemid) + '</a>';
    },
    error:function(){
      $("div#process_bar").text('ebay connect error!');
    }
  });
}

function process_list(listObj){
// initial variables
  var frame = '';
  var totalPaid = 0.00;
  var totalUnpaid = 0.00;
  var totalSales = 0.00;
  var totalShipprice = 0.00;

// process list data
  frame += '<table width="100%" cellpadding="0" cellspacing="0" id="detail">';
  for (i=0;i<listObj.orders;i++){
    if (parseFloat(listObj.order[i].paid) > 0){
      totalPaid += parseFloat(listObj.order[i].paid);
      totalShipprice += parseFloat(listObj.order[i].shipprice);
      totalSales += parseFloat(listObj.order[i].paid) - parseFloat(listObj.order[i].shipprice);
      frame += '<tr><td><div><table width="80%" align="center" style="background-color:#EEE">';
      for (k=0;k<listObj.order[i].items;k++){
        frame += '<tr><td>ItemID: ' + listObj.order[i].item[k].itemid + '</td><td>Price: ' + listObj.order[i].item[k].price + '</td></tr>';
      }
      frame += '<tr><td width="60%" colspan="2" align="center"><hr /></td></tr>';
      frame += '<tr><td colspan="2" align="right"><div>Shipping price: ' + listObj.order[i].shipprice + '</div><div>Order paid: <span style="color:#000"><b>' + listObj.order[i].paid + '</b></span></div></td></tr></table></div></td></tr>';
    }else{
      var orderUnpaid = 0.00;
      frame += '<tr><td><div><table width="80%" align="center" style="background-color:#CCC">';
      for (k=0;k<listObj.order[i].items;k++){
        orderUnpaid += parseFloat(listObj.order[i].item[k].price);
        frame += '<tr><td>ItemID: ' + listObj.order[i].item[k].itemid + '</td><td>Price: ' + listObj.order[i].item[k].price + '</td></tr>';
      }
      frame += '<tr><td width="60%" colspan="2" align="center"><hr /></td></tr>';
      frame += '<tr><td colspan="2" align="right"><div>Shipping price: ' + listObj.order[i].shipprice + '</div><div>Order paid: <span style="color:#2DC607"><b>' + listObj.order[i].paid + '</b></span></div></td></tr></table></div></td></tr>';
      orderUnpaid += parseFloat(listObj.order[i].shipprice);
      totalUnpaid += orderUnpaid;
    }
  }
  frame += '</table>';

// stuff frame
  var myDate = new Date();

  if (totalPaid > 0){
    $("div#list").html(frame);
  }
  $("div#process_bar").text('Last refrash time: ' + myDate.toLocaleString());
  $("div#total_sales").html('Total Sales: <font color="red"><b>' + totalSales.toFixed(2) + '</b></font>');
  $("div#total_unpaid").text('Total Unpaid: ' + totalUnpaid.toFixed(2));
  $("div#total_shipprice").text('Total Shipping Price: ' + totalShipprice.toFixed(2));
  $("div#total_paid").html('Total Paid: ' + totalPaid.toFixed(2));
}

function process_bar(signal){
  if (signal == true){
    $("div#process_bar").text('Loading...');
  }else{
    $("div#process_bar").text('');
  }
}

