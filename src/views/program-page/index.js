// material-ui
import { Typography } from "@mui/material";

// project imports
import MainCard from "../../ui-component/cards/MainCard";
import TrainingForm from "./trainingForm-page";

// ==============================|| RECOMMENDATION PAGE ||============================== //

const RecommendationPage = () => (
  <MainCard title="Configuration de Programme d'Entraînement & Nutrition">
    <Typography variant="body2">
      <TrainingForm />
    </Typography>
  </MainCard>
);

export default RecommendationPage;
