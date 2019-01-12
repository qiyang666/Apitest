<style scoped>
  @import './detail.css';
</style>
<style>
  @import './result.css';
</style>
<template>
    <div>
        <Table border :columns="columns3" :data="data0" class="thigh"></Table>
        <Table border ref="selection" :columns="columns4" :data="data1" class="thigh"></Table>
    </div>
</template>
<script>
export default {
  data () {
    return {
      columns4: [
        {
          title: '接口名称',
          key: 'apiname',
          width: 200,
          align: 'center'
        },
        {
          title: '接口url',
          key: 'apiurl'
        },
        {
          title: '请求方法',
          key: 'method',
          width: 120,
          align: 'center'
        },
        {
          title: '响应时间(ms)',
          key: 'response_time',
          width: 120,
          align: 'center'
        },
        {
          title: '测试结果',
          key: 'result',
          width: 120,
          align: 'center'
        },
        {
          title: '接口响应',
          key: 'action',
          width: 120,
          align: 'center',
          render: (h, params) => {
            return h('div', [
              h('Button', {
                props: {
                  type: 'default',
                  size: 'small'
                },
                style: {
                  marginRight: '5px'
                },
                on: {
                  click: () => {
                    this.preview(params.index)
                    // this.$router.push('/case/edit')
                  }
                }
              }, 'View')
            ])
          }
        }
      ],
      columns3: [
        {
          title: '用例名称',
          key: 'casename',
          width: 200,
          align: 'center'
        },
        {
          title: '项目名称',
          key: 'proname',
          align: 'center'
        },
        {
          title: '配置名称',
          key: 'confname',
          align: 'center'
        },
        {
          title: '接口级别',
          key: 'level',
          align: 'center'
        },
        {
          title: 'Total',
          key: 'total',
          align: 'center'
        },
        {
          title: 'Success',
          key: 'success',
          align: 'center'
        },
        {
          title: 'Fail',
          key: 'fail',
          align: 'center'
        },
        {
          title: '测试时间',
          key: 'time',
          align: 'center',
          width: 200
        }
      ],
      data0: [
      ],
      data1: [
      ],
      cid: localStorage.getItem('case_detail')
    }
  },
  methods: {
    preview (index) {
      const response = this.data1[index].response
      this.$Modal.info({
        width: '800',
        content: JSON.stringify(response, null, 4),
        closable: true,
        header: 'sss'
      })
    }
  },
  mounted: function () {
    // self = this;
    this.$ajax.get('/api/case/listid', {
      params: {
        id: this.cid
      }
    })
      .then((res) => {
        var tmpdata0 = {}

        if (res.data.retcode === 0) {
          for (var i = 0; i < res.data.data.result.result.length; i++) {
            var tmpResult = {}
            tmpResult['apiname'] = res.data.data.result.result[i].name
            tmpResult['apiurl'] = res.data.data.result.result[i].url
            tmpResult['method'] = res.data.data.result.result[i].method
            tmpResult['response_time'] = res.data.data.result.result[i].responsetime
            if (res.data.data.result.result[i].assert) {
              tmpResult['result'] = 'Pass'
              tmpResult['cellClassName'] = {
                result: 'result-table-success-cell-name'
              }
            } else {
              tmpResult['result'] = 'Fail'
              tmpResult['cellClassName'] = {
                result: 'result-table-fail-cell-name'
              }
            }
            tmpResult['response'] = res.data.data.result.result[i].response
            this.data1.push(tmpResult)
          }
          tmpdata0['casename'] = res.data.data.testsuitname
          tmpdata0['level'] = res.data.data.level
          tmpdata0['confname'] = res.data.data.conf
          tmpdata0['proname'] = res.data.data.proname
          tmpdata0['time'] = res.data.data.createtime
          tmpdata0['total'] = res.data.total
          tmpdata0['success'] = res.data.pass
          tmpdata0['fail'] = res.data.fail

          this.data0.push(tmpdata0)
        } else {
          this.$Notice.error({
            title: '测试详情加载失败'
          })
        }
      })
      .catch(function (error) {
        console.log(error)
      })
  }
}
</script>
