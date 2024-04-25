import React, { useEffect, useState } from 'react';
import axios from 'axios';
import {
  Container,
  Typography,
  Grid,
  Accordion,
  AccordionSummary,
  AccordionDetails,
  List,
  ListItem,
  ListItemText,
  Box
} from '@mui/material';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
 
// Composant pour l'accordéon des équipements
const EquipmentAccordion = ({ equipments }) => (
  <Accordion>
    <AccordionSummary expandIcon={<ExpandMoreIcon />}>
      <Typography variant="h4">Équipements</Typography>
    </AccordionSummary>
    <AccordionDetails>
      <List>
        {equipments.map((eq, index) => (
          <ListItem key={index}>
            <ListItemText primary={eq} />
          </ListItem>
        ))}
      </List>
    </AccordionDetails>
  </Accordion>
);
 
// Composant pour l'accordéon des ingrédients
const IngredientAccordion = ({ ingredients }) => (
  <Accordion>
    <AccordionSummary expandIcon={<ExpandMoreIcon />}>
      <Typography variant="h4">Ingrédients</Typography>
    </AccordionSummary>
    <AccordionDetails>
      <List>
        {ingredients.map((ing, index) => (
          <ListItem key={index}>
            <ListItemText primary={ing} />
          </ListItem>
        ))}
      </List>
    </AccordionDetails>
  </Accordion>
);
 
// Composant pour l'accordéon des menus
const MenuAccordion = ({ menus }) => (
  <Accordion>
    <AccordionSummary expandIcon={<ExpandMoreIcon />}>
      <Typography variant="h4">Menus de la Semaine</Typography>
    </AccordionSummary>
    <AccordionDetails>
      {Object.entries(menus).map(([day, meals]) => (
        <div key={day}>
          <Typography variant="subtitle1">{day}</Typography>
          <List>
            {meals.map((meal, mealIndex) => (
              <ListItem key={mealIndex}>
                {Object.entries(meal).map(([mealType, description], descriptionIndex) => (
                  <ListItemText
                    key={descriptionIndex}
                    primary={`${mealType}: ${description}`}
                  />
                ))}
              </ListItem>
            ))}
          </List>
        </div>
      ))}
    </AccordionDetails>
  </Accordion>
);
 
// Composant pour l'accordéon des menus
const SessionAccordion = ({ sessions_programme }) => (
  <Accordion>
    <AccordionSummary expandIcon={<ExpandMoreIcon />}>
      <Typography variant="h4">Entraînement de la Semaine</Typography>
    </AccordionSummary>
    <AccordionDetails>
      {Object.entries(sessions_programme).map(([day, exercices]) => (
        <div key={day}>
          <Typography variant="subtitle1">{day}</Typography>
          <List>
            {exercices.map((exercice, exerciceIndex) => (
              <ListItem key={exerciceIndex}>
                {Object.entries(exercice).map(([exerciceType, description], descriptionIndex) => (
                  <ListItemText
                    key={descriptionIndex}
                    primary={`${exerciceType}: ${description}`}
                  />
                ))}
              </ListItem>
            ))}
          </List>
        </div>
      ))}
    </AccordionDetails>
  </Accordion>
);
 
// Composant pour l'accordéon des programmes d'entraînement
/*const SessionAccordion = ({ sessions_programme }) => (
  <Accordion>
      <AccordionSummary expandIcon={<ExpandMoreIcon />}>
        <Typography variant="h4">Programmes d'Entraînement</Typography>
      </AccordionSummary>
      <AccordionDetails>
        {Object.entries(sessions_programme).map(([day, sessions]) => {
          if (!Array.isArray(sessions)) {
            return (
              <Typography key={day}>
                {`Les données pour ${day} ne sont pas au format attendu.`}
              </Typography>
            );
          }
 
          return (
            <div key={day}>
              <Typography variant="subtitle1">{day}</Typography>
              <List>
                {sessions.map((session, sessionIndex) => {
                  //console.log(session);
                  console.log(sessionIndex);
                  if (!session.Exercises || !Array.isArray(session.Exercises)) {
                    return (
                      <ListItem key={sessionIndex}>
                        <ListItemText primary={`Aucun exercice trouvé pour ce jour.`} />
                      </ListItem>
                    );
                  }
 
                  return (
                    <React.Fragment key={sessionIndex}>
                      {session.Exercises.map((ex, exerciseIndex) => (
                        <ListItem key={exerciseIndex}>
                          <ListItemText
                            primary={<strong>{ex.Name}</strong>}
                            secondary={ex.Description}
                          />
                        </ListItem>
                      ))}
                    </React.Fragment>
                  );
                })}
              </List>
            </div>
          );
        })}
      </AccordionDetails>
    </Accordion>
);*/
 
function Recommandation() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
 
  useEffect(() => {
    const fetchData = async () => {
      try {
        const userId = 2;
        const url = `http://127.0.0.1:5000/get-user-data/${userId}`;
        const response = await axios.get(url);
        console.log(response.data)
        setData(response.data);
        setLoading(false);
      } catch (err) {
        setError(err.message);
        setLoading(false);
        console.log(err);
      }
    };
 
    fetchData();
  }, []); // Le tableau vide signifie que cet effet se produit au chargement du composant
 
  if (loading) {
    return <Typography>Chargement...</Typography>;
  }
 
  if (error) {
    return <Typography>Erreur : {error}</Typography>;
  }
  if (!data) {
    return <Typography>Pas de données disponibles</Typography>;
  }
 
  return (
    <Container>
    <Box my={4}>
      <Typography variant="h2" align="center">
        Programme de {data.user}
      </Typography>
    </Box>
 
    <Box mt={10}>
      <Grid container spacing={3}>
        <Grid item xs={12} sm={6}>
          <SessionAccordion sessions_programme={data.sessions_programme} />
          <EquipmentAccordion equipments={data.equipments} />
        </Grid>
 
        <Grid item xs={12} sm={6}>
          <MenuAccordion menus={data.menus} />
          <IngredientAccordion ingredients={data.ingredients} />
        </Grid>
      </Grid>
    </Box>
  </Container>
  );
}
 
export default Recommandation;