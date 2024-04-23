// assets
import { IconKey } from '@tabler/icons-react';

// constant
const icons = {
  IconKey
};

// ==============================|| EXTRA PAGES MENU ITEMS ||============================== //

const pages = {
  id: 'pages',
  title: 'Menu',
  type: 'group',
  children: [
    {
      id: 'authentication',
      title: 'Authentification',
      type: 'collapse',
      icon: icons.IconKey,

      children: [
        {
          id: 'login3',
          title: 'Connexion',
          type: 'item',
          url: '/login',
          target: true
        },
        {
          id: 'register3',
          title: 'Inscription',
          type: 'item',
          url: '/register',
          target: true
        }
      ]
    }
  ]
};

export default pages;