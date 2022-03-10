-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Erstellungszeit: 10. Feb 2022 um 09:39
-- Server-Version: 10.4.22-MariaDB
-- PHP-Version: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `inzidenzen`
--
CREATE DATABASE IF NOT EXISTS `inzidenzen` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `inzidenzen`;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_belfast`
--

CREATE TABLE `inzidenzen_belfast` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_berlin`
--

CREATE TABLE `inzidenzen_berlin` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_birmingham`
--

CREATE TABLE `inzidenzen_birmingham` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_bremen`
--

CREATE TABLE `inzidenzen_bremen` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_cardiff`
--

CREATE TABLE `inzidenzen_cardiff` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_dortmund`
--

CREATE TABLE `inzidenzen_dortmund` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_dresden`
--

CREATE TABLE `inzidenzen_dresden` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_duesseldorf`
--

CREATE TABLE `inzidenzen_duesseldorf` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_edinburgh`
--

CREATE TABLE `inzidenzen_edinburgh` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_erfurt`
--

CREATE TABLE `inzidenzen_erfurt` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_essen`
--

CREATE TABLE `inzidenzen_essen` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_frankfurt`
--

CREATE TABLE `inzidenzen_frankfurt` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_glasgow`
--

CREATE TABLE `inzidenzen_glasgow` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_hamburg`
--

CREATE TABLE `inzidenzen_hamburg` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_hannover`
--

CREATE TABLE `inzidenzen_hannover` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_kiel`
--

CREATE TABLE `inzidenzen_kiel` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_koeln`
--

CREATE TABLE `inzidenzen_koeln` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_leeds`
--

CREATE TABLE `inzidenzen_leeds` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_liverpool`
--

CREATE TABLE `inzidenzen_liverpool` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_london`
--

CREATE TABLE `inzidenzen_london` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_magdeburg`
--

CREATE TABLE `inzidenzen_magdeburg` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_mainz`
--

CREATE TABLE `inzidenzen_mainz` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_manchester`
--

CREATE TABLE `inzidenzen_manchester` (
  `id` int(11) NOT NULL,
  `Datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_muenchen`
--

CREATE TABLE `inzidenzen_muenchen` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_newcastleupontyne`
--

CREATE TABLE `inzidenzen_newcastleupontyne` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_nottingham`
--

CREATE TABLE `inzidenzen_nottingham` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_portsmouth`
--

CREATE TABLE `inzidenzen_portsmouth` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_potsdam`
--

CREATE TABLE `inzidenzen_potsdam` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_saarbruecken`
--

CREATE TABLE `inzidenzen_saarbruecken` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_schwerin`
--

CREATE TABLE `inzidenzen_schwerin` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_sheffield`
--

CREATE TABLE `inzidenzen_sheffield` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_stuttgart`
--

CREATE TABLE `inzidenzen_stuttgart` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_wiesbaden`
--

CREATE TABLE `inzidenzen_wiesbaden` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `inzidenzen_belfast`
--
ALTER TABLE `inzidenzen_belfast`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_berlin`
--
ALTER TABLE `inzidenzen_berlin`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_birmingham`
--
ALTER TABLE `inzidenzen_birmingham`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_bremen`
--
ALTER TABLE `inzidenzen_bremen`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_cardiff`
--
ALTER TABLE `inzidenzen_cardiff`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_dortmund`
--
ALTER TABLE `inzidenzen_dortmund`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_dresden`
--
ALTER TABLE `inzidenzen_dresden`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_duesseldorf`
--
ALTER TABLE `inzidenzen_duesseldorf`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_edinburgh`
--
ALTER TABLE `inzidenzen_edinburgh`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_erfurt`
--
ALTER TABLE `inzidenzen_erfurt`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_essen`
--
ALTER TABLE `inzidenzen_essen`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_frankfurt`
--
ALTER TABLE `inzidenzen_frankfurt`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_glasgow`
--
ALTER TABLE `inzidenzen_glasgow`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_hamburg`
--
ALTER TABLE `inzidenzen_hamburg`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_hannover`
--
ALTER TABLE `inzidenzen_hannover`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_kiel`
--
ALTER TABLE `inzidenzen_kiel`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_koeln`
--
ALTER TABLE `inzidenzen_koeln`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_leeds`
--
ALTER TABLE `inzidenzen_leeds`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_liverpool`
--
ALTER TABLE `inzidenzen_liverpool`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_london`
--
ALTER TABLE `inzidenzen_london`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_magdeburg`
--
ALTER TABLE `inzidenzen_magdeburg`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_mainz`
--
ALTER TABLE `inzidenzen_mainz`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_manchester`
--
ALTER TABLE `inzidenzen_manchester`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_muenchen`
--
ALTER TABLE `inzidenzen_muenchen`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_newcastleupontyne`
--
ALTER TABLE `inzidenzen_newcastleupontyne`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_nottingham`
--
ALTER TABLE `inzidenzen_nottingham`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_portsmouth`
--
ALTER TABLE `inzidenzen_portsmouth`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_potsdam`
--
ALTER TABLE `inzidenzen_potsdam`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_saarbruecken`
--
ALTER TABLE `inzidenzen_saarbruecken`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_schwerin`
--
ALTER TABLE `inzidenzen_schwerin`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_sheffield`
--
ALTER TABLE `inzidenzen_sheffield`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_stuttgart`
--
ALTER TABLE `inzidenzen_stuttgart`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_wiesbaden`
--
ALTER TABLE `inzidenzen_wiesbaden`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_belfast`
--
ALTER TABLE `inzidenzen_belfast`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_berlin`
--
ALTER TABLE `inzidenzen_berlin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_birmingham`
--
ALTER TABLE `inzidenzen_birmingham`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_bremen`
--
ALTER TABLE `inzidenzen_bremen`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_cardiff`
--
ALTER TABLE `inzidenzen_cardiff`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_dortmund`
--
ALTER TABLE `inzidenzen_dortmund`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_dresden`
--
ALTER TABLE `inzidenzen_dresden`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_duesseldorf`
--
ALTER TABLE `inzidenzen_duesseldorf`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_edinburgh`
--
ALTER TABLE `inzidenzen_edinburgh`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_erfurt`
--
ALTER TABLE `inzidenzen_erfurt`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_essen`
--
ALTER TABLE `inzidenzen_essen`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_frankfurt`
--
ALTER TABLE `inzidenzen_frankfurt`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_glasgow`
--
ALTER TABLE `inzidenzen_glasgow`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_hamburg`
--
ALTER TABLE `inzidenzen_hamburg`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_hannover`
--
ALTER TABLE `inzidenzen_hannover`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_kiel`
--
ALTER TABLE `inzidenzen_kiel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_koeln`
--
ALTER TABLE `inzidenzen_koeln`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_leeds`
--
ALTER TABLE `inzidenzen_leeds`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_liverpool`
--
ALTER TABLE `inzidenzen_liverpool`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_london`
--
ALTER TABLE `inzidenzen_london`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_magdeburg`
--
ALTER TABLE `inzidenzen_magdeburg`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_mainz`
--
ALTER TABLE `inzidenzen_mainz`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_manchester`
--
ALTER TABLE `inzidenzen_manchester`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_muenchen`
--
ALTER TABLE `inzidenzen_muenchen`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_newcastleupontyne`
--
ALTER TABLE `inzidenzen_newcastleupontyne`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_nottingham`
--
ALTER TABLE `inzidenzen_nottingham`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_portsmouth`
--
ALTER TABLE `inzidenzen_portsmouth`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_potsdam`
--
ALTER TABLE `inzidenzen_potsdam`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_saarbruecken`
--
ALTER TABLE `inzidenzen_saarbruecken`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_schwerin`
--
ALTER TABLE `inzidenzen_schwerin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_sheffield`
--
ALTER TABLE `inzidenzen_sheffield`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_stuttgart`
--
ALTER TABLE `inzidenzen_stuttgart`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_wiesbaden`
--
ALTER TABLE `inzidenzen_wiesbaden`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
