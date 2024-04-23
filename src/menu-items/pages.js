// assets
import { IconKey, IconHome } from '@tabler/icons-react';

// constant
const icons = {
  IconKey, IconHome
};

// ==============================|| EXTRA PAGES MENU ITEMS ||============================== //

const pages = {
  id: 'pages',
  title: 'Menu',
  type: 'group',
  children: [
    {
      id: 'home',
      title: 'Accueil',
      type: 'item',
      icon: icons.IconHome,
      url: '/',
      breadcrumbs: false
      
    }
  ]
};

export default pages;