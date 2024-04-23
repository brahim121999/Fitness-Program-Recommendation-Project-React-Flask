// assets
import { IconBrandChrome, IconHelp, IconWindmill,IconShadow } from "@tabler/icons-react";

// constant
const icons = { IconBrandChrome, IconHelp, IconWindmill, IconShadow };

// ==============================|| SAMPLE PAGE & DOCUMENTATION MENU ITEMS ||============================== //

const other = {
  id: "sample-docs-roadmap",
  type: "group",
  children: [
    {
      id: "About",
      title: "Pourquoi TrainSmart",
      type: "item",
      url: "/",
      icon: icons.IconHelp,
      breadcrumbs: false,
    },
    {
      id: "service",
      title: "Service",
      type: "item",
      url: "/",
      icon: icons.IconWindmill,
      breadcrumbs: false,
    },
    {
      id: "programme-page",
      title: "Configurer votre Programme",
      type: "item",
      url: "/programme",
      icon: icons.IconBrandChrome,
      breadcrumbs: false,
    },
    {
      id: "recommandation",
      title: "Recommandations d'Entraînement",
      type: "item",
      url: "/recommandation",
      icon: icons.IconShadow,
      breadcrumbs: false,
    },
  ],
};

export default other;
