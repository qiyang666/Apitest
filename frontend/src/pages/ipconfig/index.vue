<style scoped>
	 @import './index.css';
</style>
<template>
	<div>
		<Button type="success" @click.native="$router.push('/ipconfig/new')">新增IP映射配置</Button>
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
                        title: '域名',
                        key: 'url'
                    },
                    {                        title: 'IP',
                        key: 'ip'
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
                                            this.$router.push('/ipconfig/edit')
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
                
                this.$ajax.get('/api/ipconfig/delete',{
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
              localStorage.setItem("ipid",`${this.data1[index].id}`)
		    },
            getIpConfList (currentPage) {
                this.$ajax.get('/api/ipconfig/list',{
                    params:{
                        page:currentPage
                    }
                })
                .then((res) => {
                    this.totalPage = parseInt(res.data.totalPageNum)*10
                    if(res.data.retcode == 0){

                        for(var i=0;i<res.data.data.length;i++){
                            var tmp = {};
                            tmp['id'] = res.data.data[i]._id
                            tmp['url'] = res.data.data[i].url
                            tmp['ip'] = res.data.data[i].iplist
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
            this.getIpConfList(defaultPage)
        },
    }
</script>