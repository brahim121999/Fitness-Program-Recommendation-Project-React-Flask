// material-ui
import { Link, Typography, Stack } from '@mui/material';

// ==============================|| FOOTER - AUTHENTICATION 2 & 3 ||============================== //

const AuthFooter = () => (
  <Stack direction="row" justifyContent="space-between">
    <Typography variant="subtitle2" component={Link} href="https://my.dauphine.fr/" target="_blank" underline="hover">
      trainSmart.fr
    </Typography>
    <Typography variant="subtitle2" component={Link} href="https://my.dauphine.fr/" target="_blank" underline="hover">
      &copy; MIAGE Dauphine
    </Typography>
  </Stack>
);

export default AuthFooter;