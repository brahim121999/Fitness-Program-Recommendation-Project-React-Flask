// material-ui
import { Typography } from '@mui/material';

// project imports
import MainCard from '../../ui-component/cards/MainCard';

// ==============================|| WELCOME PAGE ||============================== //

const WelcomePage = () => (
  <MainCard title="Accueil">
    <Typography variant="body2">
    Bienvenue sur TrainSmart !
    <br /><br />
    TrainSmart est votre compagnon ultime pour atteindre vos objectifs de fitness. Avec des séances d'entraînement personnalisées, des recommandations nutritionnelles adaptées à vos besoins. 
    <br /><br />
    TrainSmart vous aide à progresser vers une vie plus saine et plus active.
    <br /><br />
    Que vous soyez un débutant cherchant à adopter un mode de vie plus actif ou un athlète chevronné cherchant à repousser vos limites, TrainSmart est là pour vous accompagner à chaque étape de votre parcours de fitness.
    <br /><br />
    Commencez dès maintenant en vous connectant à votre compte ou en vous inscrivant pour découvrir tout ce que TrainSmart a à vous offrir.
</Typography>
  </MainCard>
);

export default WelcomePage;