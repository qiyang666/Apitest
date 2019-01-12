<style scoped>
  @import './list.css';
</style>
<style>
  @import './result.css';
</style>
<template>
    <div>
        <Button type="success" @click.native="$router.push('/case/new')">新增用例</Button>
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
          key: 'id'
        },
        {
          title: '用例名称',
          key: 'testsuitname'
        },
        {
          title: '所属项目',
          key: 'proname'
        },
        {
          title: '接口级别',
          key: 'level'
        },
        {
          title: '通用配置',
          key: 'conf'
        },
        {
          title: '测试结果',
          key: 'result'
        },
        {
          title: '跳过接口',
          key: 'skip'
        },
        {
          title: '更新时间',
          key: 'createtime',
          width: 150,
          align: 'center'
        },
        {
          title: '操作',
          key: 'action',
          width: 250,
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
                    this.$router.push('/case/edit')
                  }
                }
              }, '编辑'),
              h('Button', {
                props: {
                  type: 'info',
                  size: 'small'
                },
                style: {
                  marginRight: '5px'
                },
                on: {
                  click: () => {
                    this.run(params.row.id, params.index)
                  }
                }
              }, '测试'),
              h('Button', {
                props: {
                  type: 'success',
                  size: 'small'
                },
                style: {
                  marginRight: '5px'
                },
                on: {
                  click: () => {
                    // console.log(params.row.id)
                    this.$router.push('/case/detail')
                    this.detail(params.index)
                  }
                }
              }, '详情'),
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
      this.$ajax.get('/api/case/delete', {
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
      localStorage.setItem('case_id', `${this.data1[index].id}`)
    },
    detail (index) {
      localStorage.setItem('case_detail', `${this.data1[index].id}`)
    },
    run (cid, index) {
      this.$ajax.get('/api/case/runcase', {
        params: {
          id: cid
        }
      })
        .then((res) => {
          if (res.data.retcode === 0) {
            // console.log(res.data)
            if (res.data.status) {
              this.data1[index].result = 'Pass'
              this.data1[index].createtime = res.data.updatetime
              this.data1[index]['cellClassName'] = {result: 'result-table-success-cell-name'}
            } else {
              this.data1[index].result = 'Fail'
              this.data1[index]['cellClassName'] = {
                result: 'result-table-fail-cell-name'
              }
              this.data1[index].createtime = res.data.updatetime
            }
          } else if (res.data.retcode === 2) {
            this.$Notice.error({
              title: '接口全部跳过，没有可测试接口'
            })
          } else {
            this.$Notice.error({
              title: '测试失败'
            })
          }
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    getCaseList (currentPage) {
      this.$ajax.get('/api/case/list', {
        params: {
          page: currentPage
        }
      })
        .then((res) => {
          this.totalPage = parseInt(res.data.totalPageNum) * 10
          if (res.data.retcode === 0) {
            for (var i = 0; i < res.data.data.length; i++) {
              var tmp = {'skip': ''}
              tmp['id'] = res.data.data[i]._id
              tmp['testsuitname'] = res.data.data[i].testsuitname
              tmp['proname'] = res.data.data[i].proname
              tmp['level'] = res.data.data[i].level
              tmp['conf'] = res.data.data[i].conf

              if (res.data.data[i].result.status === true) {
                tmp['result'] = 'Pass'
                tmp['cellClassName'] = {
                  result: 'result-table-success-cell-name'
                }
                console.log(res.data.data[i].result.status)
              } else if (res.data.data[i].result.status === 'null') {
                tmp['result'] = ''
              } else {
                tmp['result'] = 'Fail'
                tmp['cellClassName'] = {
                  result: 'result-table-fail-cell-name'
                }
              }

              for (var j = 0; j < res.data.data[i].testcases.length; j++) {
                if (res.data.data[i].testcases[j].disable === 1) {
                  if (tmp['skip'] === '0') {
                    tmp['skip'] = ''
                  }
                  tmp['skip'] += res.data.data[i].testcases[j].name + ','
                }
              }
              tmp['createtime'] = res.data.data[i].createtime
              this.data1.push(tmp)
            }
          } else {
            this.$Notice.error({
              title: '用例列表加载失败'
            })
          }
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    changePage (current) {
      this.data1 = []
      this.getCaseList(current)
    }
  },
  mounted: function () {
    var defaultPage = this.currPage
    this.getCaseList(defaultPage)
  },
  computed: {
  }
}
</script>
