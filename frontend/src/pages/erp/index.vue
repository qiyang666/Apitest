<style scoped>
	 @import './index.css';
</style>
<template>
	<div>
		<Button type="success" @click.native="$router.push('/erpconfig/new')">新增账号配置</Button>
        <Table border ref="selection" :columns="columns4" :data="data1" class="thigh"></Table>
        <div style="overflow: hidden">
            <div style="float: right;">
                <Page :total="totalPage" :current="currPage" @on-change="changePage"></Page>
            </div>
        </div>
	</div>
</template>
<script>
    export default {
        data () {
            return {
                columns4: [
                    {
                        type: 'selection',
                        width: 60,
                        align: 'center',
                        key:'id'
                    },
                    {
                        title: '名称',
                        key: 'name'
                    },
                    {
                        title: '前台系统用户upk',
                        key: 'upk'
                    },
                    {   title: 'erp系统用户名',
                        key: 'username'
                    },
                    {   title: 'erp系统（加密后）密码',
                        key: 'password'
                    },
                    {   title: 'shippingId',
                        key: 'shippingId'
                    },
                    {
                    	title: '操作',
                    	key: 'action',
                    	width: 150,
                        align: 'center',
                        render:(h,params) => {
                        	return h('div',[
                        		h('Button', {
                                    props: {
                                        type: 'primary',
                                        size: 'small'
                                    },
                                    style: {
                                        marginRight: '5px'
                                    },
                                    on: {
                                        click: () => {
                                            this.preview(params.index)
                                            this.$router.push('/erpconfig/edit')
                                        },
                                    }
                                }, '编辑'),
                        		h('Button', {
                                    props: {
                                        type: 'error',
                                        size: 'small'
                                    },
                                    on: {
                                        click: () => {
                                            this.remove(params.row.id,params.index)
                                        }
                                    }
                                }, '删除')
                        	]);
                        }
                    }
                ],
                data1: [],
                currPage:1,
                totalPage:0
            }
        },
        methods: {
            handleSelectAll (status) {
                this.$refs.selection.selectAll(status);
            },
            remove (pid,index) {
                
                this.$ajax.get('/api/erp/delete',{
                    params:{
                        id:pid
                    }
                })
                .then((res) => {
                    if(res.data.retcode == 0){
                        this.data1.splice(index, 1);
                    }else{
                        this.$Notice.error({
                            title: '删除失败',
                        });
                    }
                })
                .catch(function(error){
                    console.log(error)
                });
            },
            preview (index) {
              localStorage.setItem("erp_id",`${this.data1[index].id}`)
		    },
            getErpConfList (currentPage) {
                this.$ajax.get('/api/erp/all',{
                    params:{
                        page:currentPage
                    }
                })
                .then((res) => {
                    this.totalPage = parseInt(res.data.totalPageNum)*10
                    if(res.data.retcode == 0){

                        for(var i=0;i<res.data.data.length;i++){
                            var tmp = {};
                            tmp['id'] = res.data.data[i].id
                            tmp['name'] = res.data.data[i].name
                            tmp['upk'] = res.data.data[i].upk
                            tmp['username'] = res.data.data[i].username
                            tmp['password'] = res.data.data[i].password
                            tmp['shippingId'] = res.data.data[i].shippingId
                            this.data1.push(tmp)
                        }
                    }
                })
                .catch(function(error){
                    console.log(error)
                });
            },
            changePage (current) {
                this.data1 = []
                this.getIpConfList(current)
            }
        },
        mounted:function(){
            var defaultPage = this.currPage
            this.getErpConfList(defaultPage)
        },
    }
</script>