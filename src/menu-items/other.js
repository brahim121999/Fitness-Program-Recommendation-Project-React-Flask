// assets
import { IconBrandChrome, IconHelp, IconWindmill } from '@tabler/icons-react';

// constant
const icons = { IconBrandChrome, IconHelp, IconWindmill };

// ==============================|| SAMPLE PAGE & DOCUMENTATION MENU ITEMS ||============================== //

const other = {
  id: 'sample-docs-roadmap',
  type: 'group',
  children: [
    {
      id: 'About',
      title: 'Pourquoi TrainSmart',
      type: 'item',
      url: '/',
      icon: icons.IconHelp,
      breadcrumbs: false
    },
    {
      id: 'service',
      title: 'Service',
      type: 'item',
      url: '/',
      icon: icons.IconWindmill,
      breadcrumbs: false
    },
    {
      id: 'recommendation-page',
      title: 'Fitness Recommandé',
      type: 'item',
      url: '/recommandation',
      icon: icons.IconBrandChrome,
      breadcrumbs: false
    }
  ]
};

export default other;