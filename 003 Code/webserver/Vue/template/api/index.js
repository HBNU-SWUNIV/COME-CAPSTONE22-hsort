// implement your own methods in here, if your data is coming from A rest API

import * as User from './user';


import * as Files from './file';
import * as Mail from './mail';
import * as Post from './post';
import * as Chart from './chart';








export default {
  // user
  getUser: User.getUser,
  getUserById: User.getUserById,
  // project
  // activity
  // post
  getPost: Post.getPost,

  // FIle 
  getFile: Files.getFile,
  getFileMenu: Files.getFileMenu,
  // mail
  getMail: Mail.getMail,
  getMailMenu: Mail.MailMenu,
  getMailById: Mail.getMailById,
  getMailByType: Mail.getMailByType,
  // chart data
  getMonthVisit: Chart.monthVisitData,
  getCampaign: Chart.campaignData,
  getLocation: Chart.locationData,

};