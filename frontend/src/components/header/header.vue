<style scoped>
    @import './header.css';

</style>
<template>
    <transition name="fade">
        <div class="layout">
            <Layout>
                <Header>
                    <Menu mode="horizontal" theme="dark" active-name="1">
                        <div class="layout-logo" @click="$router.push('/')">接口测试平台</div>
                        <div class="layout-nav">
                            <Submenu name="1">
                                <template slot="title">
                                  <Icon type="cube"></Icon> 项目管理
                                </template>
                                <Menu-item
                                  name="/"
                                  @click.native="$router.push('/project/list')">
                                  <Icon type="ios-list"></Icon> 项目列表
                                </Menu-item>
                                <!-- <Menu-item
                                  name="/group"
                                  @click.native="$router.push('/project/new')">
                                  <Icon type="person-stalker"></Icon> 添加项目
                                </Menu-item> -->
                            </Submenu>
                            <Submenu name="2">
                                <template slot="title">
                                  <Icon type="ios-keypad"></Icon> 测试用例管理
                                </template>
                                <Menu-item
                                  name="/case"
                                  @click.native="$router.push('/case/list')">
                                  <Icon type="ios-list"></Icon> 测试用例列表
                                </Menu-item>
                                <Menu-item
                                  name="/generate"
                                  @click.native="$router.push('/case/generate')">
                                  <Icon type="hammer"></Icon> 生成测试用例
                                </Menu-item>
                            </Submenu>
                            <Submenu name="3">
                                <template slot="title">
                                  <Icon type="ios-clock"></Icon> 定时任务管理
                                </template>
                                <Menu-item
                                  name="/crontab"
                                  @click.native="$router.push('/crontab/list')">
                                  <Icon type="ios-list"></Icon> 定时任务列表
                                </Menu-item>
                                <!-- <Menu-item
                                  name="/group"
                                  @click.native="$router.push('/group')">
                                  <Icon type="person-stalker"></Icon> 添加定时任务
                                </Menu-item> -->
                            </Submenu>
                            <Submenu name="4">
                                <template slot="title">
                                  <Icon type="pie-graph"></Icon> 统计与报告
                                </template>
                                <MenuItem
                                    name="/report"
                                    @click.native="$router.push('/report')">
                                    <Icon type="pie-graph"></Icon> 测试报告
                                </MenuItem>
                                <!-- <MenuItem
                                    name="/apiStat"
                                    @click.native="$router.push('/statistics')">
                                    <Icon type="stats-bars"></Icon> 接口统计
                                </MenuItem> -->
                            </Submenu>
                            <Submenu name="5">
                                <template slot="title">
                                  <Icon type="cube"></Icon> 工具箱
                                </template>
                                <Menu-item
                                  name="tools"
                                  @click.native="$router.push('/tools/erp')">
                                  <Icon type="ios-list"></Icon> ERP测试工具
                                </Menu-item>
                                <Menu-item
                                  name="tools"
                                  @click.native="$router.push('/jenkinsconfig/tools')">
                                  <Icon type="ios-list"></Icon> jankins构建
                                </Menu-item>

                              <!--   <Menu-item
                                  name="/group"
                                  @click.native="$router.push('/project/new')">
                                  <Icon type="person-stalker"></Icon> 添加项目
                                </Menu-item> -->
                            </Submenu>
                            <Submenu name="6">
                                <template slot="title">
                                  <Icon type="settings"></Icon> 配置管理
                                </template>
                                <Menu-item
                                    name="settings"
                                    @click.native="$router.push('/settings/list')">
                                    <Icon type="ios-list"></Icon> 通用配置
                                </Menu-item>
                                <!--<Menu-item-->
                                    <!--name="ipconfig"-->
                                    <!--@click.native="$router.push('/ipconfig/list')">-->
                                    <!--<Icon type="ios-list"></Icon> IP映射配置-->
                                <!--</Menu-item>-->
                                <!--<Menu-item-->
                                    <!--name="erpconfig"-->
                                    <!--@click.native="$router.push('/erpconfig/list')">-->
                                    <!--<Icon type="ios-list"></Icon> ERP测试配置-->
                                <!--</Menu-item>-->

                                <Menu-item
                                    name="marketconfig"
                                    @click.native="$router.push('/jenkinsconfig/list')">
                                    <Icon type="ios-list"></Icon> Jenkins任务配置
                                </Menu-item>
                            </Submenu>

                            <!-- <MenuItem name="/whiteboard" @click.native="$router.push('/whiteboard')">
                                <Icon type="ios-compose"></Icon> 需求白板
                            </MenuItem> -->
                            <!-- <Submenu name="50" class="nav-avatar">
                                <template slot="title">
                                  <img :src="userHeadImg" v-show="userHeadImg"/>
                                  <Icon type="ios-keypad"></Icon> user
                                </template>
                                <MenuItem
                                  name="/profile"
                                  @click.native="$router.push('/profile')">
                                  <Icon type="edit"></Icon> 编辑资料
                                </MenuItem>
                                <MenuItem
                                  name="/log-out"
                                  @click.native="logOut">
                                  <Icon type="log-out"></Icon> 退出
                                </MenuItem>
                            </Submenu> -->
                        </div>
                    </Menu>
                </Header>
                <Content :style="{padding: '0 50px'}">
                    <Breadcrumb :style="{margin: '20px 0'}">
                        <BreadcrumbItem>{{ bItem1 }}</BreadcrumbItem>
                        <BreadcrumbItem>{{ bItem2 }}</BreadcrumbItem>
                        <!-- <BreadcrumbItem>Layout</BreadcrumbItem> -->
                    </Breadcrumb>
                    <Card :style="{height:window_hight}">
                        <div>
                            <div class="secoo-api-status" v-show="showHome">
                                <Row :gutter="20">
                                    <Col span="12">
                                        <transition name="fadeLeft">
                                           <div class="em-dashboard__item em-dashboard__item--key">
                                               <h2><Icon type="stats-bars"></Icon>接口累积测试</h2>
                                               <p class="number">
                                                   {{ api_call_total }}
                                                   <span>次</span>
                                               </p>
                                           </div>
                                        </transition>
                                    </Col>
                                    <Col span="6">
                                        <transition name="fadeRight">
                                           <div class="em-dashboard__item">
                                               <h2><Icon type="cube"></Icon>累积项目</h2>
                                               <p class="number">
                                                    {{ project_total }}
                                                   <span>个</span>
                                               </p>
                                           </div>
                                        </transition>
                                    </Col>
                                    <Col span="6">
                                        <transition name="fadeRight">
                                           <div class="em-dashboard__item">
                                               <h2><Icon type="link"></Icon>累积接口</h2>
                                               <p class="number">
                                                   {{ api_total }}
                                                   <span>个</span>
                                               </p>
                                           </div>
                                        </transition>
                                    </Col>
                                </Row>
                            </div>
                            <transition name="fade" mode="out-in">
                                <router-view></router-view>
                            </transition>
                        </div>
                    </Card>
                </Content>
                <Footer class="layout-footer-center"><p class="em-layout__copyright">&copy; 接口自动化测试系统 乐居 | By测试部</p></Footer>
            </Layout>
        </div>
    </transition>
</template>
<script>
export default {
  data () {
    return {
      bItem1: '',
      bItem2: '',
      bItem3: '',
      api_call_total: '0',
      project_total: '0',
      api_total: '0',
      showHome: false,
      // window_hight:(window.innerHeight - 198)+'px'
      window_hight: '100%'
    }
  },
  watch: {
    '$route' (to, from) {
      var name = this.$route.name
      this.updateRoute(name)
    }
  },
  mounted: function () {
    console.log(this.window_hight)
    var name = this.$route.name
    this.updateRoute(name)
    this.getApiData()
  },
  methods: {
    getProName () {
      this.$ajax.get('/api/project/list', {
        params: {
        }
      })
        .then((res) => {
          localStorage.setItem('projectName', res.data.data[0].pro_name)
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    updateRoute (name) {
      if (name === 'newpro') {
        this.bItem1 = '项目管理'
        this.bItem2 = '添加项目'
      } else if (name === 'prolist') {
        this.bItem1 = '项目管理'
        this.bItem2 = '项目列表'
      } else if (name === 'proedit') {
        this.bItem1 = '项目管理'
        this.bItem2 = '编辑项目'
      } else if (name === 'caselist') {
        this.bItem1 = '测试用例管理'
        this.bItem2 = '测试用例列表'
      } else if (name === 'newcase') {
        this.bItem1 = '测试用例管理'
        this.bItem2 = '添加测试用例'
      } else if (name === 'caseedit') {
        this.bItem1 = '测试用例管理'
        this.bItem2 = '编辑测试用例'
      } else if (name === 'casedetail') {
        this.bItem1 = '测试用例管理'
        this.bItem2 = '测试详情'
      } else if (name === 'newcrontab') {
        this.bItem1 = '定时任务管理'
        this.bItem2 = '新增定时任务'
      } else if (name === 'crontablist') {
        this.bItem1 = '定时任务管理'
        this.bItem2 = '定时任务列表'
      } else if (name === 'crontabedit') {
        this.bItem1 = '定时任务管理'
        this.bItem2 = '编辑定时任务'
      } else if (name === 'crontabreport') {
        this.bItem1 = '定时任务管理'
        this.bItem2 = '测试报告'
      } else if (name === 'settingslist') {
        this.bItem1 = '配置管理'
        this.bItem2 = '配置文件列表'
      } else if (name === 'settingslist') {
        this.bItem1 = '配置管理'
        this.bItem2 = '配置文件列表'
      } else if (name === 'jenkinsconfig') {
        this.bItem1 = '配置管理'
        this.bItem2 = '配置列表'
      } else if (name === 'ipconfig') {
        this.bItem1 = '配置管理'
        this.bItem2 = 'ip映射配置列表'
      } else if (name === 'erpconfig') {
        this.bItem1 = '配置管理'
        this.bItem2 = 'ERP配置列表'
      } else if (name === 'erpconfignew') {
        this.bItem1 = '配置管理'
        this.bItem2 = '新增ERP账号配置'
      } else if (name === 'ipconfignew') {
        this.bItem1 = '配置管理'
        this.bItem2 = '新增IP映射配置'
      } else if (name === 'settingsedit') {
        this.bItem1 = '配置管理'
        this.bItem2 = '修改配置文件'
      } else if (name === 'toolserp') {
        this.bItem1 = '工具箱'
        this.bItem2 = 'ERP测试工具'
      } else if (name === 'report') {
        this.bItem1 = '统计与报告'
        this.bItem2 = '测试报告'
        this.getProName()
      } else if (name === 'statistics') {
        this.bItem1 = '统计与报告'
        this.bItem2 = '接口统计分析'
      } else if (name === 'whiteboard') {
        this.bItem1 = ''
        this.bItem2 = '需求白板'
      } else if (name === 'Header') {
        this.bItem2 = '首页'
        this.showHome = true
      } else {
        this.bItem2 = '首页'
      }

      if (name !== 'Header') {
        this.showHome = false
      }
    },
    getApiData () {
      this.$ajax.get('/api/analysis/listhome', {
        params: {
        }
      })
        .then((res) => {
          if (res.data.retcode === 0) {
            this.api_call_total = res.data.data.call_numbers
            this.project_total = res.data.data.project_count
            this.api_total = res.data.data.interface_count
          } else {
            console.log(res.data.message)
          }
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  }
}
</script>
