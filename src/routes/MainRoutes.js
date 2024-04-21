import { lazy } from 'react';

// project imports
import MainLayout from '../layout/MainLayout';
import Loadable from '../ui-component/Loadable';

// welcome page routing
const WelcomePage = Loadable(lazy(() => import('../views/welcome-page')));
const RecommendationPage = Loadable(lazy(() => import('../views/recommendation-page')));

// ==============================|| MAIN ROUTING ||============================== //

const MainRoutes = {
  path: '/',
  element: <MainLayout />,
  children: [
    {
      path: '/',
      element: <WelcomePage />
    },
    {
      path: '/',
      children: [
        {
          path: 'recommandation',
          element: <RecommendationPage />
        }
      ]
    }
  ]
};

export default MainRoutes;