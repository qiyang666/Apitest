import Vue from 'vue'
import Router from 'vue-router'
import Header from '@/components/header/header'
// import Home from '@/components/home/home'
// import Case from '@/components/case/case'
// import CaseList from '@/components/case/list'
// import CaseEdit from '@/components/case/edit'
// import CaseDetail from '@/components/case/detail'
// import Crontab from '@/components/crontab/crontab'
// import CrontabList from '@/components/crontab/list'
// import CrontabEdit from '@/components/crontab/edit'
// import CrontabReport from '@/components/crontab/report'
import Project from '@/components/project/project'
import ProList from '@/components/project/list'
import ProEdit from '@/components/project/editer'
// import Report from '@/components/report/report'
// import Settings from '@/components/settings/settings'
// import SettingsList from '@/components/settings/list'
// import SettingsEdit from '@/components/settings/edit'
// import Statistics from '@/components/statistics/statistics'
// import Whiteboard from '@/components/whiteboard/whiteboard'
//
// import Ipconfig from '@/pages/ipconfig/index'
// import IpconfigNew from '@/pages/ipconfig/new'
// import IpconfigEdit from '@/pages/ipconfig/edit'
// import GenerateCase from '@/pages/generate-case/index'
// import Erpconfig from '@/pages/erp/index'
// import ErpconfigNew from '@/pages/erp/new'
// import ErpconfigEdit from '@/pages/erp/edit'
// import ErpTools from '@/pages/erp/tools'
//
// import Jenkinsconfig from '@/pages/jenkinsconfig/index'
// import JenkinsconfigNew from '@/pages/jenkinsconfig/new'
// import JenkinsconfigEdit from '@/pages/jenkinsconfig/edit'
// import JenkinsconfigTools from '@/pages/jenkinsconfig/tools'
//
// import Crawler from '@/components/crawler'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    { path: '/',
      name: 'Header',
      component: Header,
      children: [
        // {path: 'home', name: 'home', component: Home},
        // { path: 'crontab/new', name: 'newcrontab', component: Crontab },
        // { path: 'crontab/list', name: 'crontablist', component: CrontabList },
        // { path: 'crontab/edit', name: 'crontabedit', component: CrontabEdit },
        // { path: 'crontab/report', name: 'crontabreport', component: CrontabReport },
        { path: 'project/new', name: 'newpro', component: Project },
        { path: 'project/list', name: 'prolist', component: ProList },
        { path: 'project/edit', name: 'proedit', component: ProEdit }
        // { path: 'case/new', name: 'newcase', component: Case },
        // { path: 'case/list', name: 'caselist', component: CaseList },
        // { path: 'case/edit', name: 'caseedit', component: CaseEdit },
        // { path: 'case/detail', name: 'casedetail', component: CaseDetail },
        // { path: 'report', name: 'report', component: Report },
        // // { path: 'report',name: 'report',component: Report },
        // { path: 'settings/new', name: 'newsettings', component: Settings },
        // { path: 'settings/list', name: 'settingslist', component: SettingsList },
        // { path: 'settings/edit', name: 'settingsedit', component: SettingsEdit },
        // { path: 'statistics', name: 'statistics', component: Statistics },
        // { path: 'whiteboard', name: 'whiteboard', component: Whiteboard },
        // { path: 'ipconfig/list', name: 'ipconfig', component: Ipconfig },
        // { path: 'ipconfig/new', name: 'ipconfignew', component: IpconfigNew },
        // { path: 'ipconfig/edit', name: 'ipconfigedit', component: IpconfigEdit },
        // { path: 'case/generate', name: 'geratercase', component: GenerateCase },
        // { path: 'erpconfig/list', name: 'erpconfig', component: Erpconfig },
        // { path: 'erpconfig/new', name: 'erpconfignew', component: ErpconfigNew },
        // { path: 'erpconfig/edit', name: 'erpconfigedit', component: ErpconfigEdit },
        // { path: 'tools/erp', name: 'toolserp', component: ErpTools },
        // { path: 'jenkinsconfig/list', name: 'jenkinsconfig', component: Jenkinsconfig },
        // { path: 'jenkinsconfig/new', name: 'jenkinsconfig', component: JenkinsconfigNew },
        // { path: 'jenkinsconfig/edit', name: 'jenkinsconfig', component: JenkinsconfigEdit },
        // { path: 'jenkinsconfig/tools', name: 'tooljenkinsconfig', component: JenkinsconfigTools }
        // { path: 'hello',name: 'hello',component: Hello },

      ]}

    // { path: '/crawler', name: 'crawler', component: Crawler}
  ]
})
