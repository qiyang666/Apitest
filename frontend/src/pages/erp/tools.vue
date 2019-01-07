<style scoped>
	 @import './index.css';
</style>
<template>
	<div class="case-zone">
		<Form :model="formItem" :label-width="140">
			<!-- <h1>选择配置</h1> -->
			<FormItem label="ERP账号配置">
	            <Select v-model="model1">
			       <Option v-for="item in ConfyList" :value="item.id" :key="item.value">{{ item.label }}</Option>
			    </Select>
		    </FormItem>
		    <h1>一键生成订单</h1>
		    <p class="declare">说明：输入商品编码和收款价格，就可以自动完成添加购物车、结算、收款等一系列操作。</p>
			<div class="box">
		        <FormItem label="商品编号">
		            <Input v-model="formItem.productid" placeholder="15941425"></Input>
		        </FormItem>
		        <FormItem label="商品收款价格">
		            <Input v-model="formItem.price" placeholder="129.00"></Input>
		        </FormItem>
		        <FormItem>
		            <Button type="primary" style="margin-left: 2px" @click="createOrder">一键下单</Button>
		            <Button type="primary" style="margin-left: 2px" @click="queryOrder">查询订单</Button>
		        </FormItem>
		        <FormItem label="">
		            <Alert>订单编号：{{ newOrderID }}</Alert>
		        </FormItem>
	        </div>

	        <h1>一键取消订单</h1> 
	        <p class="declare">说明：订单编号在不输入的情况下，默认取消该账号下所有可以取消的订单。</p>
			<div class="box">
		        <FormItem label="订单编号">
		            <Input v-model="formItem.orderid" placeholder="67789915941425"></Input>
		        </FormItem>
		        <FormItem>
		            <Button type="primary" style="margin-left: 2px" @click="cancelOrder">确定</Button>
		        </FormItem>
	        </div>
	        <h1>一键删除订单</h1>
	        <p class="declare">说明：先选择订单状态，再进行删除。</p>
	        <div class="box">     
		        <FormItem label="订单状态">
		            <Select v-model="status">
				       <Option value="已取消">已取消</Option>
				       <Option value="已完成">已完成</Option>
				    </Select>
		        </FormItem>
		        <FormItem>
		            <Button type="primary" style="margin-left: 2px" @click="deleteOrder">确定</Button>
		        </FormItem>
	        </div>
	        <h1>订单发货(联营)</h1>
	        <p class="declare">说明：从商家发货到寺库仓库。</p>
	        <div class="box">
	        	<FormItem label="商品编码">
		            <Input v-model="formItem.zf_productId" placeholder=""></Input>
		        </FormItem>   
		        <FormItem label="订单编号">
		             <Input v-model="formItem.zf_orderId" placeholder=""></Input>
		        </FormItem>
		        <FormItem>
		            <Button type="primary" style="margin-left: 2px" @click="lySendOut">确定</Button>
		        </FormItem>
	        </div>
	        <h1>订单发货(自营)</h1>
	        <p class="declare">说明：使用顺序先发货、再签收,最后完成,可用于自营发货。(不包括解挂功能)</p>
	        <div class="box">  
	        	<!-- <FormItem label="商家类型">
		            <Select v-model="signin">
				       <Option value="自营">自营</Option>
				       <Option value="联营">联营</Option>
				    </Select>
		        </FormItem>  -->
		        <FormItem label="选择仓库">
		        	<Select v-model="ware">
		            	<Option v-for="item in wareList" :value="item.id" :key="item.value">{{ item.label }}</Option>
		            </Select>
		        </FormItem>  
		      <!--   <FormItem label="商家编码">
		            <Input v-model="formItem.orderid"></Input> 
		        </FormItem> -->
		        <FormItem label="订单编号">
		            <Input v-model="formItem.sendOrderId"></Input> 
		        </FormItem>
		        <FormItem>
		            <Button type="primary" style="margin-left: 2px" @click="sendOut">发货</Button>
		            <Button type="primary" style="margin-left: 2px" @click="signOff">签收</Button>
		            <Button type="primary" style="margin-left: 2px" @click="sendOutOk">完成</Button>
		        </FormItem>
	        </div>
	        <h1>欧洲自营商家对接测试</h1>
	        <p class="declare">说明：该功能仅用于欧洲自营商家对接测试。</p>
	        <div class="box"> 
	        	<!-- <h3 class="sub-title">添加新商家</h3> -->
		        <FormItem label="订单编号">
		            <Input v-model="lockOrderId" placeholder=""></Input>
		        </FormItem>
		        <FormItem label="商品编号">
		            <Input v-model="lockProductId" placeholder=""></Input>
		         </FormItem>
		        <FormItem>
		            <Button type="primary" style="margin-left: 2px" @click="syncOrder">订单同步</Button>
		            <Button type="primary" style="margin-left: 2px" @click="lockOrder">测试订单锁库</Button>
		            <Button type="primary" style="margin-left: 2px" @click="updateStock">更新库存</Button>
		            <Button type="primary" style="margin-left: 2px" @click="syncStock">测试库存同步</Button>
		        </FormItem>
	        </div>
		</Form>
	</div>
</template>
<script>

    export default {
      data () {
      	return {
      		index:1,
      		formItem:{
      			id:'',
      			productid:'',
      			price:'',
      			orderid:'',
      			sendOrderId:'',
      			zf_orderId:'',
      			zf_productId:''
      		},
      		ConfyList:[
      			
      		],
      		wareList:[
      			{"id":1,"value":"华北大仓区","label":"华北大仓区"},
      			{"id":2,"value":"北京仓","label":"北京仓"},
      			{"id":3,"value":"上海仓","label":"上海仓"},
      			{"id":4,"value":"成都仓","label":"成都仓"},
      			{"id":6,"value":"香港仓","label":"香港仓"},
      			{"id":7,"value":"美国纽约仓","label":"美国纽约仓"},
      			{"id":8,"value":"日本大阪仓","label":"日本大阪仓"},
      			{"id":9,"value":"GS仓","label":"GS仓"},
      			{"id":10,"value":"法国巴黎仓","label":"法国巴黎仓"},
      			{"id":11,"value":"韩国仓","label":"韩国仓"},
      			{"id":12,"value":"华东大区仓","label":"华东大区仓"},
      			{"id":13,"value":"海外虚拟仓","label":"海外虚拟仓"},
      			{"id":14,"value":"澳洲仓","label":"澳洲仓"},
      			{"id":15,"value":"新西兰仓","label":"新西兰仓"},
      			{"id":16,"value":"深圳保税仓","label":"深圳保税仓"},
      			{"id":17,"value":"香港中心仓","label":"香港中心仓"},
      			{"id":18,"value":"马来西亚门店仓","label":"马来西亚门店仓"},
      			{"id":19,"value":"香港二店","label":"香港二店"},
      			{"id":20,"value":"宜春仓","label":"宜春仓"},
      			{"id":21,"value":"深圳仓","label":"深圳仓"},
      			{"id":22,"value":"青岛仓","label":"青岛仓"},
      			{"id":23,"value":"天津仓","label":"天津仓"},
      			{"id":24,"value":"厦门仓","label":"厦门仓"},
      			{"id":25,"value":"长沙仓","label":"长沙仓"},
      			{"id":26,"value":"意大利米兰仓","label":"意大利米兰仓"},
      			{"id":27,"value":"米兰店","label":"米兰店"},
      			{"id":28,"value":"马来西亚仓","label":"马来西亚仓"},
      		],
      		orderStatus:[
      			{"id":"1","value":"已完成","label":"已完成"},
      			{"id":"1","value":"已取消","label":"已取消"}
      		],
      		model1:'',
      		status:'',
      		newOrderID:'',
      		syncOrderId:'',
      		lockOrderId:'',
      		lockProductId:'',
      		signin:'',
      		returns:'',
      		ware:''
      	}
      },
      methods:{
		createOrder () {
			this.$ajax.get('/api/erp/createorder',{
                params:{
                	id:this.model1,
                    productid:this.formItem.productid,
                    price:this.formItem.price,
                }
            })
            .then((res) => {
            	var msg = ''
            	for (var i=1;i<res.data.result.length;i++){
            		msg+=res.data.result[i].msg+','
            	}	
            	this.$Notice.error({
                    title: msg,
                });
            })
            .catch(function(error){
                console.log(error)
            });
		},
		cancelOrder () {
			this.$ajax.get('/api/erp/cancelorder',{
                params:{
                    orderid:this.formItem.orderid,
                    id:this.model1,
                }
            })
            .then((res) => {
            	if(res.data.success == 1){
            		this.$Notice.error({
	                    title: '无需要取消的订单',
	                });
            	}else if(res.data.success == 2){
            		this.$Notice.error({	
	                    title: '订单接口异常,无响应',
	                });
            	}else{
            		var msg = ''
	            	for (var i=0;i<res.data.result.length;i++){
	            		msg+=res.data.result[i].msg+','
	            	}	
	            	this.$Notice.error({
	                    title: msg,
	                });
            	}
            })
            .catch(function(error){
                console.log(error)
            });
		},
		deleteOrder () {
			this.$Notice.error({
                title: '开始删除订单中。。。',
            });
			this.$ajax.get('/api/erp/delorder',{
                params:{
                    type:this.status,
                    id:this.model1,
                }
            })
            .then((res) => {
            	if(res.data.success == 0){
            		this.$Notice.error({
	                    title: '订单删除成功',
	                });
            	}else if(res.data.success == 1){
            		this.$Notice.error({
	                    title: '订单删除失败',
	                });
            	}else{
            		this.$Notice.error({
	                    title: '没有可以删除的订单',
	                });
            	}
            })
            .catch(function(error){
                console.log(error)
            });
		},
		getConfigList () {
			this.$ajax.get('/api/erp/all',{
                params:{
                    page:'1'
                }
            })
            .then((res) => {
            	this.model1 = res.data.data[0].name
            	for(var i=0;i<res.data.data.length;i++){
            		var tmp = {};
            		tmp['id'] = res.data.data[i].id
            		tmp['value'] = res.data.data[i].name
                    tmp['label'] = res.data.data[i].name
                    this.ConfyList.push(tmp)
            	}
            })
            .catch(function(error){
                console.log(error)
            });
		},
		queryOrder () {
			this.$ajax.get('/api/erp/queryorderid',{
                params:{
                	id:this.model1,
                }
            })
            .then((res) => {

            	if(res.data.retcode == 0){
            		this.newOrderID = res.data.neworderid
            	}else if(res.data.retcode == 1) {
            		this.$Notice.error({
	                    title: '该用户无订单',
	                });
            	}else{
            		this.$Notice.error({
	                    title: '未选择用户或者订单接口异常。',
	                });
            	}
            })
            .catch(function(error){
                console.log(error)
            });
		},
		syncOrder () {
			this.$ajax.get('/api/erp/syncOrderid',{
                params:{
                	id:this.model1,
                	orderid:this.lockOrderId
                }
            })
            .then((res) => {
            	if(res.data.sucess == 0){
            		console.log(res.data)
            		this.$Notice.info({
	                    title: '订单同步成功',
	                });
            	}else{
            		this.$Notice.error({
	                    title: '订单同步失败。',
	                });
            	}
            })
            .catch(function(error){
                console.log(error)
            });
		},
		lockOrder () {
			this.$ajax.get('/api/erp/querylockstock',{
                params:{
                	// id:this.model1,
                	orderid:this.lockOrderId,
                	productid:this.lockProductId
                }
            })
            .then((res) => {
            	if(res.data.success == 0){
	                if(res.data.result[0].request_flag == 1){
            			this.$Notice.info({
		                    title: '订单锁库成功',
		                });
            		}else{
            			this.$Notice.info({
		                    title: '订单锁库失败',
		                });
            		}
            	}else if(res.data.success == 1){
            		this.$Notice.info({
	                    title: '订单还未同步,请先同步订单或者稍后再试',
	                });
            	}else if(res.data.success == 2){
            		this.$Notice.info({
	                    title: '锁库数据，还未写入完成',
	                });
            	}else if(res.data.success == 3){
            		this.$Notice.info({
	                    title: 't_rfq不能存在此订单稍后再试',
	                });
            	}else{
            		this.$Notice.error({
	                    title: '参数错误',
	                });
            	}
            })
            .catch(function(error){
                console.log(error)
            });
		},
		updateStock () {
			this.$ajax.get('/api/erp/updatestock',{
                params:{
                	productid:this.lockProductId
                }
            })
            .then((res) => {
            	if(res.data.sucess == 0){
            		console.log(res.data.spu_sizestock,res.data.stocktb_stock)
            		localStorage.setItem('spu_size_stock',res.data.spu_sizestock)
            		localStorage.setItem('tb_stock',res.data.spu_sizestock)
            		this.$Notice.info({
	                    title: '商品库存修改成功',
	                });
            	}else{
            		this.$Notice.error({
	                    title: '商品编号不存在或者修改库存失败。',
	                });
            	}
            })
            .catch(function(error){
                console.log(error)
            });
		},
		syncStock () {
			this.$ajax.get('/api/erp/teststock',{
                params:{
                	productid:this.lockProductId,
                	spu_size_stock:localStorage.getItem('spu_size_stock'),
                	oldstocktb:localStorage.getItem('tb_stock')
                }
            })
            .then((res) => {
            	console.log(res.data)
            	this.$Notice.info({
                    title: res.data.message,
                });
            })
            .catch(function(error){
                console.log(error)
            });
		},
		sendOut () {
			console.log(this.ware)
			console.log(this.signin);
			this.$ajax.get('/api/erp/sendgoods',{
                params:{
                	id:this.model1,
                	code:this.ware,
                	orderid:this.formItem.sendOrderId
                }
            })
            .then((res) => {
            	console.log(res.data)
            	this.$Notice.info({
                    title: res.data.message,
                });
            })
            .catch(function(error){
                console.log(error)
            });
		},
		signOff () {
			this.$ajax.get('/api/erp/ordersign',{
                params:{
                	id:this.model1,
                	orderid:this.formItem.sendOrderId
                }
            })
            .then((res) => {
            	console.log(res.data)
            	this.$Notice.info({
                    title: res.data.message,
                });
            })
            .catch(function(error){
                console.log(error)
            });
		},
		sendOutOk () {
			this.$ajax.get('/api/erp/ordercomplete',{
                params:{
                	id:this.model1,
                	orderid:this.formItem.sendOrderId
                }
            })
            .then((res) => {
            	console.log(res.data)
            	this.$Notice.info({
                    title: res.data.message,
                });
            })
            .catch(function(error){
                console.log(error)
            });
		},
		lySendOut () {
			this.$ajax.get('/api/erp/lysendgoods',{
                params:{
                	id:this.model1,
                	product:this.formItem.zf_productId,
                	orderid:this.formItem.zf_orderId
                }
            })
            .then((res) => {
            	console.log(res.data)
            	this.$Notice.info({
                    title: res.data.message,
                });
            })
            .catch(function(error){
                console.log(error)
            });
		}
	  },
	  mounted:function(){
        this.getConfigList()
      },
    }
</script>