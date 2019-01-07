<style scoped>
  @import './list.css';
</style>
<template>
    <div>
        <Button type="success" @click.native="$router.push('/project/new')">新增项目</Button>
        <Table border ref="selection" :columns="columns4" :data="data1" class="thigh"></Table>
        <div style="overflow: hidden">
            <div style="float: right;">
                <Page :total="totalPage" :current="currPage" @on-change="changePage"></Page>
            </div>
        </div>
        <!-- <Button @click="handleSelectAll(true)">全部选择</Button>
        <Button @click="handleSelectAll(false)">取消全选</Button>
        <Page :current="2" :total="50" simple></Page> -->
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
          key: 'id'
        },
        {
          title: '项目名称',
          key: 'pro_name'
        },
        {
          title: '测试人员',
          key: 'tester'
        },
        {
          title: '开发人员',
          key: 'developer'
        },
        {
          title: '报警邮箱',
          key: 'receive_mail'
        },
        {
          title: '钉钉机器人地址',
          key: 'dingding'
        },
        {
          title: '项目描述',
          key: 'pro_detail'
        },
        {
          title: '创建时间',
          key: 'create_time'
        },
        {
          title: '操作',
          key: 'action',
          width: 150,
          align: 'center',
          render: (h, params) => {
            return h('div', [
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
                    // this.show(params.index)
                    this.preview(params.index)
                    this.$router.push('/project/edit')
                  }
                }
              }, '编辑'),
              h('Button', {
                props: {
                  type: 'error',
                  size: 'small'
                },
                on: {
                  click: () => {
                    // console.log(params.row.id)
                    this.remove(params.row.id, params.index)
                  }
                }
              }, '删除')
            ])
          }
        }
      ],
      data1: [
      ],
      data2: '',
      currPage: 1,
      totalPage: 0
    }
  },
  methods: {
    handleSelectAll (status) {
      this.$refs.selection.selectAll(status)
    },
    show (index) {
      const content = `Name：${this.data1[index].name}<br>Age：${this.data1[index].age}<br>Address：${this.data1[index].address}<br>Date：${this.data1[index].date}<br>Name：<input value=${this.data1[index].name} style="width: 600px" />`
      this.$Modal.confirm({
        // title: 'Project Info',
        width: '800',
        content: content
      })
    },
    remove (pid, index) {
      this.$ajax.get('/api/project/delete', {
        params: {
          id: pid
        }
      })
        .then((res) => {
          if (res.data.retcode === 0) {
            this.data1.splice(index, 1)
          }
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    preview (index) {
      localStorage.setItem('pid', `${this.data1[index].id}`)
      localStorage.setItem('pro_name', `${this.data1[index].pro_name}`)
      localStorage.setItem('tester', `${this.data1[index].tester}`)
      localStorage.setItem('developer', `${this.data1[index].developer}`)
      localStorage.setItem('receive_mail', `${this.data1[index].receive_mail}`)
      localStorage.setItem('dingding', `${this.data1[index].dingding}`)
      localStorage.setItem('pro_detail', `${this.data1[index].pro_detail}`)
    },
    getProList (currentPage) {
      this.$ajax.get('/api/project/list', {
        params: {
          page: currentPage
        }
      })
        .then((res) => {
          this.data1 = res.data.data
          this.totalPage = parseInt(res.data.totalPageNum) * 10
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    changePage (current) {
      this.getProList(current)
    }
  },
  mounted: function () {
    var defaultPage = this.currPage
    this.getProList(defaultPage)
  }
}
</script>
